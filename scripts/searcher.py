import time
import random
from selenium.webdriver.common.by import By
from scripts.query_generator import generate_smart_query  # 🆕 Import AI query generator

def perform_searches(browser, topics_list, num_searches=30, smart_mode=True):
    base_url = "https://www.bing.com/search?q="

    for i in range(num_searches):
        if smart_mode:
            topic = random.choice(topics_list)
            query = generate_smart_query(topic)
        else:
            query = random.choice(topics_list)

        search_url = base_url + query.replace(' ', '+')

        browser.get(search_url)
        print(f"🔎 Searching: {query} ({i+1}/{num_searches})")

        time.sleep(random.uniform(2, 5))  # random wait between searches
