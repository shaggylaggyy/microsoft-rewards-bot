from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import random

def create_browser(mobile=False):
    options = Options()
    options.use_chromium = True
    options.add_argument("--headless=new")  # 🧙‍♂️ Enable headless mode (invisible browser)
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications")

    if mobile:
        mobile_emulation = {
            "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
            "userAgent": "Mozilla/5.0 (Linux; Android 10; Mobile) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36"
        }
        options.add_experimental_option("mobileEmulation", mobile_emulation)

    service = Service(EdgeChromiumDriverManager().install())
    browser = webdriver.Edge(service=service, options=options)

    return browser
