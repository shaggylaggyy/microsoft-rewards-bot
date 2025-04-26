import os
import time
import random
import schedule
from datetime import datetime
from scripts.browser_manager import create_browser
from scripts.login_manager import login
from scripts.searcher import perform_searches
from scripts.promotions import complete_promotions
from scripts.notifier import send_discord_notification
from scripts.utils import load_json, load_search_topics, get_random_greeting
from scripts.points_logger import log_points  # 🆕 Added for Points Logging

# Paths
SETTINGS_PATH = os.path.join("config", "settings.json")
ACCOUNTS_PATH = os.path.join("config", "accounts.json")
TOPICS_PATH = os.path.join("config", "search_topics.txt")

# Load config
settings = load_json(SETTINGS_PATH)
accounts = load_json(ACCOUNTS_PATH)
topics = load_search_topics(TOPICS_PATH)

REGION = settings.get("region", "en-US")
SMART_MODE = settings.get("smart_mode", True)
WEBHOOK_URL = settings.get("discord_webhook_url", None)
DAILY_RUN_TIME = settings.get("daily_run_time", "08:00")

# Fake point tracking for now (will be dynamic later)
POINTS_PER_ACCOUNT = 500  # 🛠️ Temporary placeholder until real points scraping is added

def farm_account(account):
    email = account["email"]
    password = account["password"]

    print(f"➡️ Starting farming for: {email}")
    print(get_random_greeting())

    # Desktop farming
    browser = create_browser(mobile=False)
    if login(browser, email, password):
        complete_promotions(browser)
        perform_searches(browser, topics, num_searches=30, smart_mode=SMART_MODE)
    browser.quit()
    time.sleep(random.uniform(5, 10))

    # Mobile farming
    browser = create_browser(mobile=True)
    if login(browser, email, password):
        perform_searches(browser, topics, num_searches=20, smart_mode=SMART_MODE)
    browser.quit()

    print(f"✅ Finished farming for: {email}")

def farm_all_accounts():
    print(f"\n📅 Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🛠️ Farming {len(accounts)} account(s)...\n")

    for account in accounts:
        farm_account(account)

    # 🆕 Log today's points (simplified for now)
    total_points = len(accounts) * POINTS_PER_ACCOUNT
    log_points(total_points)

    # Discord notification
    if WEBHOOK_URL:
        send_discord_notification(WEBHOOK_URL, f"✅ Farming complete! Total points today: {total_points}")

    print("\n👋 All farming done for today!\n")

def main():
    import sys
    if len(sys.argv) > 1 and sys.argv[1].lower() == "now":
        farm_all_accounts()
    else:
        print(f"⏰ Scheduled farming at {DAILY_RUN_TIME} daily.")
        schedule.every().day.at(DAILY_RUN_TIME).do(farm_all_accounts)

        while True:
            schedule.run_pending()
            time.sleep(60)

if __name__ == "__main__":
    main()
