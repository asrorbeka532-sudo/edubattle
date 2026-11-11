import os
import sys
import io
import json
import base64
import hashlib
import zipfile
import datetime
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import pkcs7, Encoding
from androguard.core.apk import APK

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_APK_PATH = os.path.join(ROOT_DIR, "backend", "EduBattle.apk")

print(f"Reading base APK: {BASE_APK_PATH}")
zin = zipfile.ZipFile(BASE_APK_PATH, "r")

files = {}
for item in zin.infolist():
    # Strip existing signatures
    if item.filename.startswith("META-INF/"):
        continue
    files[item.filename] = zin.read(item.filename)

zin.close()
print(f"Loaded {len(files)} files from base APK.")

# 1. Modify AndroidManifest.xml:
# Set targetSdkVersion=34, compileSdkVersion=34, platformBuildVersionCode=34
axml = bytearray(files["AndroidManifest.xml"])
# Offsets discovered in analysis:
# 3228: compileSdkVersion
# 3288: platformBuildVersionCode
# 3384: targetSdkVersion
axml[3228] = 34
axml[3288] = 34
axml[3384] = 34
files["AndroidManifest.xml"] = bytes(axml)
print("Updated AndroidManifest.xml: compileSdkVersion=34, platformBuildVersionCode=34, targetSdkVersion=34")

# 2. Modify resources.arsc:
# Replace "My WebView" with "Edu Battle" (offset 13297, exactly 10 ASCII bytes)
arsc = bytearray(files["resources.arsc"])
pos = arsc.find(b"\n\nMy WebView\x00")
if pos != -1:
    arsc[pos : pos + 13] = b"\n\nEdu Battle\x00"
    print(f"Updated resources.arsc at offset {pos}: 'My WebView' -> 'Edu Battle'")
else:
    # Alternative direct offset
    if arsc[13297:13307] == b"My WebView":
        arsc[13297:13307] = b"Edu Battle"
        print("Updated resources.arsc at offset 13297: 'My WebView' -> 'Edu Battle'")
    else:
        print("Warning: 'My WebView' string not found at expected offset!")
files["resources.arsc"] = bytes(arsc)

# 3. Create EduBattle assets/web/index.html
edubattle_web_index = """<!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Edu Battle</title>
    <style>
        :root {
            --bg-dark: #0a0e1a;
            --card-bg: #131c31;
            --card-border: rgba(99, 102, 241, 0.25);
            --primary: #6366f1;
            --primary-glow: rgba(99, 102, 241, 0.4);
            --secondary: #ec4899;
            --accent: #10b981;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --danger: #ef4444;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            -webkit-tap-highlight-color: transparent;
        }

        body {
            background-color: var(--bg-dark);
            color: var(--text-main);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
            background-image: 
                radial-gradient(circle at 10% 20%, rgba(99, 102, 241, 0.15) 0%, transparent 40%),
                radial-gradient(circle at 90% 80%, rgba(236, 72, 153, 0.15) 0%, transparent 40%);
        }

        .container {
            width: 100%;
            max-width: 440px;
            background: var(--card-bg);
            border: 1px solid var(--card-border);
            border-radius: 24px;
            padding: 32px 24px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.45);
            text-align: center;
            position: relative;
            overflow: hidden;
        }

        .container::before {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(90deg, var(--primary), var(--secondary), var(--accent));
        }

        .logo-wrap {
            margin-bottom: 20px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 80px;
            height: 80px;
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.2), rgba(236, 72, 153, 0.2));
            border: 2px solid var(--primary);
            border-radius: 22px;
            box-shadow: 0 0 25px var(--primary-glow);
        }

        .logo-icon {
            font-size: 40px;
        }

        h1 {
            font-size: 26px;
            font-weight: 800;
            margin-bottom: 8px;
            background: linear-gradient(135deg, #fff 0%, #cbd5e1 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            letter-spacing: -0.5px;
        }

        .badge {
            display: inline-block;
            background: rgba(99, 102, 241, 0.15);
            border: 1px solid rgba(99, 102, 241, 0.3);
            color: #a5b4fc;
            padding: 4px 14px;
            border-radius: 100px;
            font-size: 12px;
            font-weight: 600;
            margin-bottom: 18px;
        }

        p.desc {
            color: var(--text-muted);
            font-size: 14px;
            line-height: 1.5;
            margin-bottom: 24px;
        }

        .status-box {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            padding: 12px;
            border-radius: 14px;
            background: rgba(0, 0, 0, 0.25);
            margin-bottom: 22px;
            font-size: 13px;
        }

        .status-dot {
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background: #fbbf24;
            box-shadow: 0 0 10px #fbbf24;
            animation: pulse 1.5s infinite;
        }

        .status-dot.online {
            background: var(--accent);
            box-shadow: 0 0 10px var(--accent);
        }

        .status-dot.offline {
            background: var(--danger);
            box-shadow: 0 0 10px var(--danger);
        }

        @keyframes pulse {
            0%, 100% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.5; transform: scale(0.9); }
        }

        .form-group {
            text-align: left;
            margin-bottom: 18px;
        }

        label {
            display: block;
            font-size: 12px;
            font-weight: 600;
            color: var(--text-muted);
            margin-bottom: 6px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        input {
            width: 100%;
            padding: 14px 16px;
            background: rgba(15, 23, 42, 0.8);
            border: 1px solid var(--card-border);
            border-radius: 12px;
            color: var(--text-main);
            font-size: 14px;
            outline: none;
            transition: all 0.2s;
        }

        input:focus {
            border-color: var(--primary);
            box-shadow: 0 0 15px var(--primary-glow);
        }

        .btn {
            display: block;
            width: 100%;
            padding: 14px;
            border-radius: 14px;
            border: none;
            font-size: 15px;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s ease;
            text-decoration: none;
            margin-bottom: 10px;
        }

        .btn-primary {
            background: linear-gradient(135deg, var(--primary) 0%, #4f46e5 100%);
            color: white;
            box-shadow: 0 4px 15px var(--primary-glow);
        }

        .btn-primary:active {
            transform: scale(0.98);
        }

        .btn-outline {
            background: transparent;
            color: var(--text-muted);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        .btn-outline:active {
            background: rgba(255, 255, 255, 0.05);
        }

        .loader {
            display: inline-block;
            width: 18px;
            height: 18px;
            border: 2px solid rgba(255, 255, 255, 0.3);
            border-radius: 50%;
            border-top-color: #fff;
            animation: spin 0.8s linear infinite;
            vertical-align: middle;
            margin-right: 8px;
        }

        @keyframes spin {
            to { transform: rotate(360deg); }
        }

        .footer {
            margin-top: 18px;
            font-size: 11px;
            color: #64748b;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo-wrap">
            <span class="logo-icon">⚡</span>
        </div>
        <h1>Edu Battle</h1>
        <div class="badge">Rasmiy Mobil Ilova v1.20</div>
        
        <p class="desc">Intellektual onlayn fanlar jangi va avtomatlashtirilgan bilim bellashuvi platformasi.</p>

        <div class="status-box">
            <div id="statusDot" class="status-dot"></div>
            <span id="statusText">Serverga ulanish tekshirilmoqda...</span>
        </div>

        <form id="connectForm" onsubmit="handleConnect(event)">
            <div class="form-group">
                <label for="serverUrl">EduBattle Server Manzili</label>
                <input type="text" id="serverUrl" placeholder="http://192.168.100.101:8000" spellcheck="false" autocomplete="off">
            </div>

            <button type="submit" id="btnConnect" class="btn btn-primary">
                <span id="btnLoader" class="loader" style="display:none;"></span>
                <span id="btnLabel">🚀 Platformaga kirish</span>
            </button>
            <button type="button" onclick="loadDefaultLocal()" class="btn btn-outline">
                🔄 Standart serverni tiklash
            </button>
        </form>

        <div class="footer">
            EduBattle Security Protected &bull; Android 14 API 34
        </div>
    </div>

    <script>
        const DEFAULT_SERVER = "http://192.168.100.101:8000";

        function getSavedServer() {
            return localStorage.getItem("edubattle_server_url") || DEFAULT_SERVER;
        }

        function setSavedServer(url) {
            localStorage.setItem("edubattle_server_url", url);
        }

        const input = document.getElementById("serverUrl");
        const statusDot = document.getElementById("statusDot");
        const statusText = document.getElementById("statusText");
        const btnLoader = document.getElementById("btnLoader");
        const btnLabel = document.getElementById("btnLabel");

        input.value = getSavedServer();

        async function probeServer(url, timeoutMs = 2500) {
            const controller = new AbortController();
            const timer = setTimeout(() => controller.abort(), timeoutMs);
            try {
                const target = url.replace(/\\/+$/, "") + "/api/sync/state";
                const res = await fetch(target, { signal: controller.signal, mode: 'cors' });
                clearTimeout(timer);
                return res.ok;
            } catch (err) {
                clearTimeout(timer);
                return false;
            }
        }

        async function autoConnect() {
            const currentUrl = input.value.trim().replace(/\\/+$/, "");
            statusDot.className = "status-dot";
            statusText.innerText = "Server tekshirilmoqda...";
            btnLoader.style.display = "inline-block";
            btnLabel.innerText = "Ulanmoqda...";

            const isAlive = await probeServer(currentUrl, 2000);
            btnLoader.style.display = "none";
            btnLabel.innerText = "🚀 Platformaga kirish";

            if (isAlive) {
                statusDot.className = "status-dot online";
                statusText.innerText = "Server faol! Yuklanmoqda...";
                setTimeout(() => {
                    window.location.replace(currentUrl + "/");
                }, 400);
            } else {
                statusDot.className = "status-dot offline";
                statusText.innerText = "Serverga ulanib bo'lmadi. Wi-Fi yoki IP ni tekshiring.";
            }
        }

        async function handleConnect(e) {
            if (e) e.preventDefault();
            let url = input.value.trim();
            if (!url) url = DEFAULT_SERVER;
            if (!url.startsWith("http://") && !url.startsWith("https://")) {
                url = "http://" + url;
            }
            url = url.replace(/\\/+$/, "");
            input.value = url;
            setSavedServer(url);

            statusDot.className = "status-dot";
            statusText.innerText = "Ulanmoqda: " + url;
            btnLoader.style.display = "inline-block";
            btnLabel.innerText = "Tekshirilmoqda...";

            const isAlive = await probeServer(url, 3000);
            btnLoader.style.display = "none";
            btnLabel.innerText = "🚀 Platformaga kirish";

            if (isAlive) {
                statusDot.className = "status-dot online";
                statusText.innerText = "Ulandi! O'tilmoqda...";
                window.location.replace(url + "/");
            } else {
                statusDot.className = "status-dot offline";
                statusText.innerText = "Server javob bermadi (" + url + ")";
            }
        }

        function loadDefaultLocal() {
            input.value = DEFAULT_SERVER;
            setSavedServer(DEFAULT_SERVER);
            autoConnect();
        }

        // Run auto connection after 200ms
        setTimeout(autoConnect, 200);
    </script>
</body>
</html>
"""

files["assets/web/index.html"] = edubattle_web_index.encode("utf-8")
print("Updated assets/web/index.html with EduBattle Launcher UI.")

# 4. Update assets/settings.json
settings_json = {
    "sites": [
        {
            "url": "http://192.168.100.101:8000/",
            "title": "Edu Battle"
        },
        {
            "url": "https://appassets.androidplatform.net/assets/web/index.html",
            "title": "Edu Battle Launcher"
        }
    ],
    "other": "http://192.168.100.101:8000/",
    "match": [
        ["host", "equals", "appassets.androidplatform.net"],
        ["host", "contains", "192.168."],
        ["host", "equals", "localhost"],
        ["host", "equals", "10.0.2.2"],
        ["host", "contains", "edubattle"],
        ["host", "contains", "ngrok"],
        ["host", "contains", "loca.lt"]
    ],
    "skip": [
        ["path", "endsWith", ".epub"]
    ],
    "remote_debug": True,
    "console_log": False,
    "js_interface": False,
    "context_menu": False,
    "not_matching": False,
    "local_sites": True,
    "update_zip": "",
    "web_settings": {
        "JavaScriptEnabled": True,
        "DomStorageEnabled": True,
        "DatabaseEnabled": True
    },
    "source": "assets",
    "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat()
}

files["assets/settings.json"] = json.dumps(settings_json, indent=2).encode("utf-8")
print("Updated assets/settings.json with EduBattle endpoints and match filters.")

# 5. Sign APK (v1 JAR/PKCS#7 signature)
print("Computing cryptographic digests and creating signatures...")
manifest_mf = bytearray(b"Manifest-Version: 1.0\r\nCreated-By: 1.0 (EduBattle)\r\n\r\n")
cert_sf = bytearray(b"Signature-Version: 1.0\r\nCreated-By: 1.0 (EduBattle)\r\n")

mf_entries = {}
for name in sorted(files.keys()):
    data = files[name]
    sha256 = base64.b64encode(hashlib.sha256(data).digest()).decode("ascii")
    sha1 = base64.b64encode(hashlib.sha1(data).digest()).decode("ascii")
    entry = f"Name: {name}\r\nSHA-256-Digest: {sha256}\r\nSHA1-Digest: {sha1}\r\n\r\n".encode("utf-8")
    mf_entries[name] = entry
    manifest_mf.extend(entry)

mf_sha256 = base64.b64encode(hashlib.sha256(manifest_mf).digest()).decode("ascii")
mf_sha1 = base64.b64encode(hashlib.sha1(manifest_mf).digest()).decode("ascii")
cert_sf.extend(f"SHA-256-Digest-Manifest: {mf_sha256}\r\nSHA1-Digest-Manifest: {mf_sha1}\r\n\r\n".encode("utf-8"))

for name in sorted(files.keys()):
    entry = mf_entries[name]
    entry_sha256 = base64.b64encode(hashlib.sha256(entry).digest()).decode("ascii")
    entry_sha1 = base64.b64encode(hashlib.sha1(entry).digest()).decode("ascii")
    cert_sf.extend(f"Name: {name}\r\nSHA-256-Digest: {entry_sha256}\r\nSHA1-Digest: {entry_sha1}\r\n\r\n".encode("utf-8"))

# Generate RSA-2048 key and self-signed certificate
key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, "UZ"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "Tashkent"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, "EduBattle Platform"),
    x509.NameAttribute(NameOID.COMMON_NAME, "EduBattle Official Release"),
])

cert = x509.CertificateBuilder().subject_name(
    subject
).issuer_name(
    issuer
).public_key(
    key.public_key()
).serial_number(
    x509.random_serial_number()
).not_valid_before(
    datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=1)
).not_valid_after(
    datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=10000)
).sign(key, hashes.SHA256())

builder = pkcs7.PKCS7SignatureBuilder().set_data(bytes(cert_sf))
builder = builder.add_signer(cert, key, hashes.SHA256())
cert_rsa = builder.sign(Encoding.DER, options=[pkcs7.PKCS7Options.DetachedSignature, pkcs7.PKCS7Options.Binary])

# 6. Build target APK file bytes
buf = io.BytesIO()
zout = zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED)
zout.writestr("META-INF/MANIFEST.MF", bytes(manifest_mf))
zout.writestr("META-INF/CERT.SF", bytes(cert_sf))
zout.writestr("META-INF/CERT.RSA", cert_rsa)

for name in sorted(files.keys()):
    zout.writestr(name, files[name])
zout.close()

signed_apk_bytes = buf.getvalue()
print(f"Generated clean signed APK: {len(signed_apk_bytes)} bytes")

# 7. Validate with Androguard
test_apk = APK(signed_apk_bytes, raw=True)
print("--- APK VALIDATION REPORT ---")
print(f"App Name:       {test_apk.get_app_name()}")
print(f"Package:        {test_apk.get_package()}")
print(f"Target SDK:     {test_apk.get_target_sdk_version()} (Android 14)")
print(f"Min SDK:        {test_apk.get_min_sdk_version()}")
print(f"Signed:         {test_apk.is_signed()}")
print(f"Signed v1:      {test_apk.is_signed_v1()}")

assert test_apk.get_app_name() == "Edu Battle", f"App name mismatch: {test_apk.get_app_name()}"
assert str(test_apk.get_target_sdk_version()) == "34", f"Target SDK mismatch: {test_apk.get_target_sdk_version()}"
assert test_apk.is_signed() is True, "APK is not signed!"

# 8. Save signed APK to all target locations
destinations = [
    os.path.join(ROOT_DIR, "backend", "EduBattle.apk"),
    os.path.join(ROOT_DIR, "frontend", "downloads", "EduBattle.apk"),
    os.path.join(ROOT_DIR, "EduBattle.apk"),
]

for dest in destinations:
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "wb") as f:
        f.write(signed_apk_bytes)
    print(f"Successfully saved to: {dest} ({len(signed_apk_bytes)} bytes)")

print("\nSUCCESS: All EduBattle APKs built, patched, signed, and deployed!")
