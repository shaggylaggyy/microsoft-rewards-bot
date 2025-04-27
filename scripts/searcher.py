import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from scripts.query_generator import generate_smart_query

# Define basic topics for search variety
BASE_TOPICS = [
    "technology", "sports", "health", "movies", "news", "games",
    "travel", "music", "education", "history", "food", "science"
]

def perform_searches(browser, mobile=False):
    try:
        search_count = 30 if not mobile else 20

        if mobile:
            print("📱 Farming mobile searches...")
        else:
            print("🖥️ Farming desktop searches...")

        browser.get('https://www.bing.com/')
        time.sleep(random.uniform(3, 5))

        for i in range(search_count):
            base_topic = random.choice(BASE_TOPICS)
            query = generate_smart_query(base_topic)  # ✅ Pass base_topic now

            search_box = browser.find_element(By.NAME, "q")
            search_box.clear()
            search_box.send_keys(query)
            search_box.send_keys(Keys.RETURN)

            print(f"🔎 Searching: {query} ({i+1}/{search_count})")

            time.sleep(random.uniform(3, 6))  # Human-like random sleep

            browser.get('https://www.bing.com/')
            time.sleep(random.uniform(2, 4))

    except Exception as e:
        print(f"⚠️ Error during searching: {e}")
