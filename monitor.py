import requests
import subprocess

# ===== CONFIG =====
GEMINI_API_KEY = "AIzaSyBGdq0kBA5r_JyFdS9mRn3cFmWxZ8r0ukQ"
FONNTE_TOKEN = "o1stvLQK8sKeCPkbTSDe"
WHATSAPP_TARGET = "6289627468600"
# ==================

def send_whatsapp(msg):
    url = "https://api.fonnte.com/send"
    data = {"target": WHATSAPP_TARGET, "message": msg}
    headers = {"Authorization": FONNTE_TOKEN}
    requests.post(url, data=data, headers=headers)

def gemini_analyze(text):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateText?key={GEMINI_API_KEY}"
    payload = {"prompt": {"text": text}}
    res = requests.post(url, json=payload).json()

    try:
        return res["candidates"][0]["outputText"]
    except:
        return "AI analysis failed."

def check_once():
    logs = subprocess.getoutput("sudo grep 'Failed password' /var/log/auth.log | tail -n 20")
    if logs:
        summary = gemini_analyze("Summarize this SSH attack log: " + logs)
        send_whatsapp("🚨 SSH Attack Detected!\n\n" + summary)

check_once()
