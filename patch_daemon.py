import re

with open('run_bot_daemon.py', 'r', encoding='utf-8') as f:
    code = f.read()

old_check = '''    # 3. Check tunnel URL
    new_url = extract_tunnel_url_from_log(cf_log)
    if new_url:
        current_url = get_current_redirect_tunnel_url()
        logging.info(f"Current Netlify Tunnel: {current_url} | Active Cloudflare Tunnel: {new_url}")
        if current_url != new_url:
            try:
                update_and_deploy_netlify(new_url)
            except Exception as e:
                logging.error(f"Failed to auto-deploy Netlify: {e}")'''

new_check = '''    # 3. Wait and extract tunnel URL with retries
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
                logging.error(f"Failed to auto-deploy Netlify: {e}")'''

code = code.replace(old_check, new_check, 1)

# Also in the periodic while True loop, check if tunnel URL changed!
old_loop = '''    # Self-healing loop every 60 seconds
    while True:
        try:
            time.sleep(60)
            if not is_port_in_use(8000) or not is_process_running("cloudflared.exe"):
                logging.warning("Service outage detected! Auto-restarting...")
                start_services()
        except Exception as e:
            logging.error(f"Loop error: {e}")
            time.sleep(10)'''

new_loop = '''    # Self-healing loop every 30 seconds
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
            time.sleep(10)'''

code = code.replace(old_loop, new_loop, 1)

with open('run_bot_daemon.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated run_bot_daemon.py")
