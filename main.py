# main.py

import time
from scripts.browser_manager import create_browser
from scripts.login_manager import login
from scripts.promotions import complete_daily_set, complete_punch_cards, complete_promotions
from scripts.searcher import perform_searches
from scripts.points_logger import log_points
from scripts.notifier import send_discord_notification
import json

def farm_account(account, selected_task):
    browser = create_browser(mobile=False)

    if login(browser, account['email'], account['password']):
        print(f"🚀 Logged in successfully: {account['email']}")

        if selected_task == "1":
            complete_daily_set(browser)
        elif selected_task == "2":
            complete_punch_cards(browser)
        elif selected_task == "3":
            complete_promotions(browser)
        elif selected_task == "4":
            perform_searches(browser, mobile=False)
            perform_searches(browser, mobile=True)
        elif selected_task == "5":
            log_points(browser)
        elif selected_task == "6":
            # Full farming
            complete_daily_set(browser)
            complete_punch_cards(browser)
            complete_promotions(browser)
            perform_searches(browser, mobile=False)
            perform_searches(browser, mobile=True)
            log_points(browser)

        # ✅ Send Discord Notification after task
        send_discord_notification(account['email'], f"Task {selected_task} completed successfully ✅")
    
    else:
        print(f"❌ Login failed for {account['email']}")

    browser.quit()

def farm_all_accounts(selected_task):
    with open("config/accounts.json", "r") as f:
        accounts = json.load(f)

    print(f"📅 Starting farming for {len(accounts)} account(s)...")

    for account in accounts:
        print(f"➡️ Starting farming for: {account['email']}")
        farm_account(account, selected_task)

def show_menu():
    print("\n🧠 Please choose what you want to do:")
    print("1️⃣ Complete Daily Set only")
    print("2️⃣ Complete Punch Cards only")
    print("3️⃣ Complete Promotions only")
    print("4️⃣ Perform Desktop + Mobile Searches only")
    print("5️⃣ Log Points only")
    print("6️⃣ Farm Everything (FULL)")
    choice = input("\n👉 Enter your choice (1-6): ").strip()
    return choice

def main():
    selected_task = show_menu()
    farm_all_accounts(selected_task)

if __name__ == "__main__":
    main()
