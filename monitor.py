import requests
import subprocess
import time

# ===============================
# CONFIGURASI
# ===============================
GEMINI_API_KEY = "MASUKKAN_API_KEY_GEMINI_KAMU"
FONNTE_TOKEN = "MASUKKAN_TOKEN_FONNTE_KAMU"
WHATSAPP_TARGET = "62xxxxxxxxxx"  # nomor WA penerima
# ===============================


def send_whatsapp(message):
    url = "https://api.fonnte.com/send"
    data = {"target": WHATSAPP_TARGET, "message": message}
    headers = {"Authorization": FONNTE_TOKEN}
    requests.post(url, data=data, headers=headers)


def gemini_analyze(text):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateText?key={GEMINI_API_KEY}"
    payload = {"prompt": {"text": text}}
    result = requests.post(url, json=payload).json()
    try:
        return result["candidates"][0]["outputText"]
    except:
        return "AI analysis failed."


def check_ssh_attacks():
    logs = subprocess.getoutput("sudo grep 'Failed password' /var/log/auth.log | tail -n 20")
    if logs:
        summary = gemini_analyze("Please summarize this server SSH attack log: " + logs)
        send_whatsapp("🚨 *SSH Attack Detected!*\n\n" + summary)


while True:
    check_ssh_attacks()
    time.sleep(30)
