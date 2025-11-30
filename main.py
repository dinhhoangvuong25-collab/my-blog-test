import os
import json
import pickle
import subprocess
import requests

# Hardcoded secret (High severity)
API_KEY = "123456-SECRET-KEY-HARDCODED"

def run_system_command(user_input):
    """
    CRITICAL: Command Injection.
    """
    command = f"echo User said: {user_input} >> /tmp/log.txt"
    # Không kiểm tra input, cho vào shell → command injection
    os.system(command)
    return "Command executed"

def insecure_deserialize(payload):
    """
    CRITICAL: Arbitrary Code Execution via pickle
    """
    return pickle.loads(payload)  # Snyk sẽ flag ngay

def fetch_unsecure(url):
    """
    High/Medium: Insecure HTTP (no TLS)
    """
    response = requests.get(url)  # Không HTTPS
    return response.text

def main():
    print("App started with vulnerabilities.")

    # --- CRITICAL: Lấy input trực tiếp từ user rồi đẩy vào shell ---
    user_input = os.getenv("USER_INPUT", "default; rm -rf /")
    run_system_command(user_input)

    # --- CRITICAL: Deserialization ---
    malicious_payload = os.getenv("PICKLE_DATA", b"\x80\x04K.")
    insecure_deserialize(malicious_payload)

    # --- High severity: HTTP insecure ---
    data = fetch_unsecure("http://example.com")

    print("Finished.")

if __name__ == "__main__":
    main()
