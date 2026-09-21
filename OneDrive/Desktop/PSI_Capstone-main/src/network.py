import hashlib
import os
import socket
import requests


def fetch_uuid():
    """Fetch a random UUID from external API."""
    print("\n--- Fetching UUID from API ---")
    try:
        # استخدام API بديل ومستقر للـ UUID
        r = requests.get("https://uuid.rocks/json", timeout=5)
        r.raise_for_status()
        uuid_val = r.json().get("uuid")
        print(f"[+] UUID Received: {uuid_val}")
        return uuid_val
    except Exception as e:
        print(f"[!] API Request failed: {e}")
        return None


def quick_check(path, host, port):
    """Calculate SHA256 of a file and check socket connection on target port."""
    print("\n--- Artifact Integrity & Port Check ---")

    # 1. Calculate SHA256
    if not os.path.exists(path):
        with open(path, "w") as f:
            f.write("test content\n")

    with open(path, "rb") as f:
        file_hash = hashlib.sha256(f.read()).hexdigest()

    # 2. Check Port Status
    s = socket.socket()
    s.settimeout(2)
    try:
        status = "open" if s.connect_ex((host, int(port))) == 0 else "closed"
    except Exception as e:
        status = f"error ({e})"
    finally:
        s.close()

    result = {"sha256": file_hash, "port_status": status}
    print(f"[+] SHA256 Hash: {result['sha256']}\n[+] Port {port} Status: {result['port_status']}")
    return result