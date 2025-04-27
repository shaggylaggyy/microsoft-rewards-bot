# promotions.py

import time
import random
from selenium.webdriver.common.by import By

def complete_daily_set(browser):
    try:
        print("🛠️ Completing Daily Set...")
        browser.get('https://rewards.bing.com/')
        time.sleep(random.uniform(5, 7))  # Let page fully load

        # Find the daily-sets section
        try:
            daily_sets_section = browser.find_element(By.ID, "daily-sets")
        except Exception:
            print("⚠️ Daily Sets section not found!")
            return

        # Find the first mee-card-group inside daily-sets (today's activities)
        try:
            today_set_group = daily_sets_section.find_element(By.CSS_SELECTOR, "mee-card-group")
        except Exception:
            print("⚠️ Today's set group not found!")
            return

        # Inside that group, find the mee-cards
        daily_set_cards = today_set_group.find_elements(By.CSS_SELECTOR, "mee-card")

        if not daily_set_cards:
            print("⚠️ No Daily Set activities found!")
            return

        print(f"🔎 Found {len(daily_set_cards)} daily set activities!")

        for index in range(len(daily_set_cards)):
            try:
                print(f"➡️ Clicking activity {index+1}")

                # Re-find everything fresh each loop
                browser.get('https://rewards.bing.com/')
                time.sleep(random.uniform(5, 7))

                daily_sets_section = browser.find_element(By.ID, "daily-sets")
                today_set_group = daily_sets_section.find_element(By.CSS_SELECTOR, "mee-card-group")
                daily_set_cards = today_set_group.find_elements(By.CSS_SELECTOR, "mee-card")

                card = daily_set_cards[index]

                browser.execute_script("arguments[0].scrollIntoView(true);", card)
                time.sleep(1)

                clickable = card.find_element(By.TAG_NAME, "a")
                clickable.click()

                time.sleep(random.uniform(6, 8))  # Let task page load

                solve_opened_task(browser)

            except Exception as e:
                print(f"⚠️ Error during activity {index+1}: {e}")
                continue

    except Exception as e:
        print(f"⚠️ Error completing daily set: {e}")

def solve_opened_task(browser):
    try:
        time.sleep(5)  # Let page load

        # Check for quiz buttons
        options = browser.find_elements(By.CSS_SELECTOR, "div[class*='rq_option']")
        if options:
            print("🧠 Solving quiz...")
            random.choice(options).click()
            time.sleep(random.uniform(4, 6))
            return

        # Check for poll options
        vote_buttons = browser.find_elements(By.CSS_SELECTOR, "div[class*='bt_option']")
        if vote_buttons:
            print("🧠 Voting poll...")
            random.choice(vote_buttons).click()
            time.sleep(random.uniform(4, 6))
            return

        # If just article
        print("📰 Reading article...")
        time.sleep(random.uniform(10, 15))

    except Exception as e:
        print(f"⚠️ Error solving task: {e}")

def complete_punch_cards(browser):
    try:
        print("🎯 Completing Punch Cards...")
        browser.get('https://rewards.bing.com/')
        time.sleep(random.uniform(5, 7))

        punch_cards = browser.find_elements(By.CSS_SELECTOR, "a[class*='task-link']")
        print(f"🔎 Found {len(punch_cards)} punch card tasks!")

        for index, card in enumerate(punch_cards):
            try:
                card.click()
                print(f"➡️ Clicking punch card {index+1}")
                time.sleep(random.uniform(6, 8))
                browser.back()
                time.sleep(random.uniform(5, 7))
            except Exception as e:
                print(f"⚠️ Error during punch card {index+1}: {e}")
                continue

    except Exception as e:
        print(f"⚠️ Error completing punch cards: {e}")

def complete_promotions(browser):
    try:
        print("🎯 Completing Other Promotions...")
        browser.get('https://rewards.bing.com/')
        time.sleep(random.uniform(5, 7))

        promos = browser.find_elements(By.CSS_SELECTOR, "a[class*='task-link']")
        print(f"🔎 Found {len(promos)} promotions!")

        for index, promo in enumerate(promos):
            try:
                promo.click()
                print(f"➡️ Clicking promo {index+1}")
                time.sleep(random.uniform(6, 8))
                browser.back()
                time.sleep(random.uniform(5, 7))
            except Exception as e:
                print(f"⚠️ Error during promo {index+1}: {e}")
                continue

    except Exception as e:
        print(f"⚠️ Error completing promotions: {e}")
