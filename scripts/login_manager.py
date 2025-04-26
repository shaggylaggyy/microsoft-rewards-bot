import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(browser, email, password):
    try:
        # Go directly to Rewards login
        browser.get('https://rewards.microsoft.com')

        wait = WebDriverWait(browser, 10)
        time.sleep(3)

        # Check if already logged in
        if "rewards" in browser.current_url or "bing.com" in browser.current_url:
            print("✅ Already logged in, skipping login.")
            return True

        # Otherwise, try to login
        # Find and click "Sign In" button manually
        try:
            sign_in_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign in")))
            sign_in_button.click()
            print("➡️ Clicking Sign In button...")
            time.sleep(3)
        except Exception as e:
            print("⚠️ Sign In button not found, assuming already signed in.")
            return True

        # Wait for email input
        email_input = wait.until(EC.presence_of_element_located((By.NAME, 'loginfmt')))
        email_input.send_keys(email)
        browser.find_element(By.ID, 'idSIButton9').click()

        # Wait for password input
        password_input = wait.until(EC.presence_of_element_located((By.NAME, 'passwd')))
        password_input.send_keys(password)
        browser.find_element(By.ID, 'idSIButton9').click()

        try:
            stay_signed_in = wait.until(EC.element_to_be_clickable((By.ID, 'idSIButton9')))
            stay_signed_in.click()
        except Exception:
            pass

        time.sleep(3)
        return True

    except Exception as e:
        print(f"❌ Login failed for {email}: {e}")
        return False
