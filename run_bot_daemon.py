import os
import sys
import time
import socket
import subprocess
import re
import json
import zipfile
import urllib.request
import logging

logging.basicConfig(
    filename='daemon.log',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
BIN_CLOUDFLARED = os.path.join(PROJECT_DIR, "bin", "cloudflared.exe")
NETLIFY_TOKEN = "nfp_4H1C3vRWFRafSLrFqdRmE9qf5sRgYnZV4b72"
NETLIFY_SITE_ID = "f643d9e4-a1a6-48e8-8981-3cc5560d6d7a"

def is_port_in_use(port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1.0)
            return s.connect_ex(('127.0.0.1', port)) == 0
    except Exception:
        return False

def is_process_running(proc_name):
    try:
        out = subprocess.check_output(f'tasklist /FI "IMAGENAME eq {proc_name}"', shell=True, text=True)
        return proc_name.lower() in out.lower()
    except Exception:
        return False

def get_current_redirect_tunnel_url():
    redir_file = os.path.join(PROJECT_DIR, "frontend", "_redirects")
    if os.path.exists(redir_file):
        with open(redir_file, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith("/api/*"):
                    m = re.search(r'https://([a-zA-Z0-9-]+)\.trycloudflare\.com', line)
                    if m:
                        return m.group(0)
    return None

def update_and_deploy_netlify(new_tunnel_url):
    logging.info(f"Updating Netlify configuration to new tunnel URL: {new_tunnel_url}")
    
    # 1. Update frontend/_redirects
    redir_file = os.path.join(PROJECT_DIR, "frontend", "_redirects")
    redir_content = (
        f"/api/*  {new_tunnel_url}/api/:splat  200!\n"
        f"/uploads/*  {new_tunnel_url}/uploads/:splat  200\n"
        f"/apk  /downloads/EduBattle.apk  302\n"
        f"/app  /  302\n"
        f"/download  /download.html  200\n"
        f"/*  /index.html  200\n"
    )
    with open(redir_file, 'w', encoding='utf-8') as f:
        f.write(redir_content)

    # 2. Update netlify.toml
    toml_file = os.path.join(PROJECT_DIR, "netlify.toml")
    toml_content = f"""[build]
  publish = "frontend"

[[redirects]]
  from = "/api/*"
  to = "{new_tunnel_url}/api/:splat"
  status = 200
  force = true

[[redirects]]
  from = "/uploads/*"
  to = "{new_tunnel_url}/uploads/:splat"
  status = 200
  force = false

[[redirects]]
  from = "/apk"
  to = "/downloads/EduBattle.apk"
  status = 302

[[redirects]]
  from = "/app"
  to = "/"
  status = 302

[[redirects]]
  from = "/download"
  to = "/download.html"
  status = 200

[[headers]]
  for = "/downloads/*.apk"
  [headers.values]
    Content-Type = "application/vnd.android.package-archive"
    Content-Disposition = "attachment; filename=\\"EduBattle.apk\\""
    Cache-Control = "public, max-age=31536000"

[[headers]]
  for = "/*"
  [headers.values]
    Access-Control-Allow-Origin = "*"
    Access-Control-Allow-Methods = "GET, POST, PUT, DELETE, OPTIONS"
    Access-Control-Allow-Headers = "*"
"""
    with open(toml_file, 'w', encoding='utf-8') as f:
        f.write(toml_content)

    # 3. Update frontend/js/app.js BACKEND_TUNNEL_URL
    app_js_file = os.path.join(PROJECT_DIR, "frontend", "js", "app.js")
    if os.path.exists(app_js_file):
        with open(app_js_file, 'r', encoding='utf-8') as f:
            app_code = f.read()
        app_code = re.sub(
            r'const BACKEND_TUNNEL_URL = [\'"]https://[a-zA-Z0-9-]+\.trycloudflare\.com[\'"];',
            f"const BACKEND_TUNNEL_URL = '{new_tunnel_url}';",
            app_code
        )
        with open(app_js_file, 'w', encoding='utf-8') as f:
            f.write(app_code)

    # 4. Create deploy zip (lean 3MB)
    zip_path = os.path.join(PROJECT_DIR, "deploy_auto.zip")
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
        for root, dirs, files in os.walk(os.path.join(PROJECT_DIR, 'frontend')):
            for f in files:
                full_p = os.path.join(root, f)
                rel_p = os.path.relpath(full_p, os.path.join(PROJECT_DIR, 'frontend'))
                if f.lower().endswith('.pdf') or f.lower().endswith('.apk'):
                    continue
                z.write(full_p, rel_p)

    # 5. Upload deploy to Netlify
    deploy_url = f"https://api.netlify.com/api/v1/sites/{NETLIFY_SITE_ID}/deploys"
    with open(zip_path, 'rb') as f:
        data = f.read()
    
    req = urllib.request.Request(
        deploy_url,
        data=data,
        headers={
            "Content-Type": "application/zip",
            "Authorization": f"Bearer {NETLIFY_TOKEN}"
        },
        method="POST"
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        res = json.loads(resp.read().decode('utf-8'))
        logging.info(f"Netlify deploy complete! State: {res.get('state')}, ID: {res.get('id')}")

def extract_tunnel_url_from_log(log_path):
    if not os.path.exists(log_path):
        return None
    try:
        with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        m = re.findall(r'https://([a-zA-Z0-9-]+)\.trycloudflare\.com', content)
        if m:
            return f"https://{m[-1]}.trycloudflare.com"
    except Exception as e:
        logging.error(f"Error reading tunnel log: {e}")
    return None

def start_services():
    os.chdir(PROJECT_DIR)
    python_exe = sys.executable
    cf_log = os.path.join(PROJECT_DIR, "tunnel.log")

    # 1. Start uvicorn backend if not running
    if not is_port_in_use(8000):
        logging.info("Starting uvicorn backend...")
        subprocess.Popen(
            [python_exe, "-m", "uvicorn", "backend.app:app", "--host", "0.0.0.0", "--port", "8000"],
            cwd=PROJECT_DIR,
            creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0
        )
        time.sleep(3)

    # 2. Start cloudflared if not running
    if not is_process_running("cloudflared.exe"):
        logging.info("Starting cloudflared tunnel...")
        if os.path.exists(BIN_CLOUDFLARED):
            with open(cf_log, "w", encoding="utf-8") as out_f:
                subprocess.Popen(
                    [BIN_CLOUDFLARED, "tunnel", "--url", "http://127.0.0.1:8000"],
                    cwd=PROJECT_DIR,
                    stdout=out_f,
                    stderr=subprocess.STDOUT,
                    creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0
                )
            time.sleep(6)

    # 3. Wait and extract tunnel URL with retries
    new_url = None
    for _ in range(15):
        new_url = extract_tunnel_url_from_log(cf_log)
        if new_url:
            break
        time.sleep(2)

    if new_url:
        current_url = get_current_redirect_tunnel_url()
        logging.info(f"Current Netlify Tunnel: {current_url} | Active Cloudflare Tunnel: {new_url}")
        if current_url != new_url:
            try:
                update_and_deploy_netlify(new_url)
            except Exception as e:
                logging.error(f"Failed to auto-deploy Netlify: {e}")

if __name__ == '__main__':
    logging.info("EduBattle Master Daemon started.")
    time.sleep(3)
    start_services()

    # Self-healing loop every 30 seconds
    while True:
        try:
            time.sleep(30)
            if not is_port_in_use(8000) or not is_process_running("cloudflared.exe"):
                logging.warning("Service outage detected! Auto-restarting...")
                start_services()
            else:
                cf_log = os.path.join(PROJECT_DIR, "tunnel.log")
                active_url = extract_tunnel_url_from_log(cf_log)
                if active_url:
                    current_url = get_current_redirect_tunnel_url()
                    if active_url != current_url:
                        logging.info(f"Tunnel URL change detected in loop: {current_url} -> {active_url}")
                        update_and_deploy_netlify(active_url)
        except Exception as e:
            logging.error(f"Loop error: {e}")
            time.sleep(10)
