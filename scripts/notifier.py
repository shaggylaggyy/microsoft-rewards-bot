import requests

def send_discord_notification(webhook_url, message):
    data = {
        "content": message
    }
    try:
        response = requests.post(webhook_url, json=data)
        if response.status_code == 204:
            print("📨 Discord notification sent successfully!")
        else:
            print(f"❌ Failed to send Discord notification: {response.text}")
    except Exception as e:
        print(f"❌ Error sending Discord notification: {e}")
