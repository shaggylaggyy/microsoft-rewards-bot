import requests
import json

# Load settings
with open("config/settings.json", "r") as f:
    settings = json.load(f)

WEBHOOK_URL = settings["discord_webhook_url"]

def send_discord_notification(email, message):
    if not WEBHOOK_URL:
        print("❗ No Discord Webhook URL configured.")
        return

    payload = {
        "username": "Microsoft Rewards Bot 🤖",
        "content": f"📨 **{email}**\n{message}"
    }
    try:
        response = requests.post(WEBHOOK_URL, json=payload)
        if response.status_code == 204:
            print("📨 Discord notification sent successfully!")
        else:
            print(f"⚠️ Discord webhook failed with status code: {response.status_code}")
    except Exception as e:
        print(f"⚠️ Error sending Discord notification: {e}")
