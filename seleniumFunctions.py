from selenium.webdriver.common.by import By
import time

def log_into_existing_account(driver, email, password):
    """
    Logs into an existing account using the provided email and password.

    Args:
        driver: The Selenium WebDriver instance.
        email: The email address of the account.
        password: The password of the account.
    """

    # Find the login button element by its ID and click it
    login_button = driver.find_element(By.ID, 'log-in')
    login_button.click()
    time.sleep(1) # Wait for 1 second

    # Find the email input field by its ID and enter the email
    email = driver.find_element(By.ID, 'email')
    email.send_keys(email)
    time.sleep(0.75) # Wait for 0.75 seconds

    # Find the password input field by its ID and enter the password
    password = driver.find_element(By.ID, 'password')
    password.send_keys(password)
    time.sleep(0.75) # Wait for 0.75 seconds

    # Find the login button element by its CSS selector and click it
    login_button = driver.find_element(By.CSS_SELECTOR, '.aws-btn.aws-btn--primary.aws-btn--visible.false.aws-btn--progress')
    login_button.click()
    time.sleep(4) # Wait for 4 seconds to allow the page to load