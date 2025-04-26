import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def complete_promotions(browser):
    try:
        browser.get("https://rewards.microsoft.com/")
        wait = WebDriverWait(browser, 10)
        time.sleep(3)

        print("🎉 Promotions page opened.")

        # Find all promotion cards
        cards = browser.find_elements(By.CSS_SELECTOR, "a.mee-card.mee-card-clickable")

        for idx, card in enumerate(cards):
            try:
                print(f"🎯 Clicking promotion {idx + 1}...")
                card.click()
                time.sleep(random.uniform(3, 5))

                # Handle quizzes (if quiz detected)
                if "quiz" in browser.current_url or "trivia" in browser.current_url:
                    complete_quiz(browser)
                
                # Handle polls
                elif "poll" in browser.current_url:
                    complete_poll(browser)

                else:
                    # Just stay for a few seconds if it's a simple promotion
                    time.sleep(3)

                browser.back()
                time.sleep(3)

            except Exception as e:
                print(f"⚠️ Failed to complete promotion {idx + 1}: {e}")
                browser.back()
                continue

    except Exception as e:
        print(f"❌ Failed to open promotions page: {e}")

def complete_quiz(browser):
    try:
        wait = WebDriverWait(browser, 10)
        # Answer a few questions randomly
        for _ in range(3):
            options = browser.find_elements(By.CSS_SELECTOR, "button")
            if options:
                random.choice(options).click()
                time.sleep(random.uniform(2, 4))
            else:
                break
    except Exception as e:
        print(f"⚠️ Quiz error: {e}")

def complete_poll(browser):
    try:
        wait = WebDriverWait(browser, 10)
        options = browser.find_elements(By.CSS_SELECTOR, "button")
        if options:
            random.choice(options).click()
            time.sleep(2)
    except Exception as e:
        print(f"⚠️ Poll error: {e}")
