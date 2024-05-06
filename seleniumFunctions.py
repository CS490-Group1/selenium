from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import random

def log_into_existing_account(driver, user_email, user_password):
    """
    Logs into an existing account using the provided email and password.

    Args:
        driver: The Selenium WebDriver instance.
        user_email: The email address of the account.
        user_password: The password of the account.
    """

    # Find the login button element by its ID and click it
    login_button = driver.find_element(By.ID, 'log-in')
    login_button.click()
    time.sleep(1) # Wait for 1 second

    # Find the email input field by its ID and enter the email
    email_field = driver.find_element(By.ID, 'email')
    email_field.send_keys(user_email)
    time.sleep(0.75) # Wait for 0.75 seconds

    # Find the password input field by its ID and enter the password
    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys(user_password)
    time.sleep(0.75) # Wait for 0.75 seconds

    # Find the login button element by its CSS selector and click it
    login_button = driver.find_element(By.CSS_SELECTOR, '.aws-btn.aws-btn--primary.aws-btn--visible.false.aws-btn--progress')
    login_button.click()
    time.sleep(4) # Wait for 4 seconds to allow the page to load



def select_random_vehicle(driver):
    """
    Selects a random vehicle from a list of vehicles on the webpage.

    Args:
        driver: The Selenium WebDriver instance.

    Returns:
        None
    """

    random_number = random.randint(5, 100) # Generate a random number between 5 and 100
    # Find all the vehicle elements by their CSS selector and click the random vehicle
    random_vehicle = driver.find_elements(By.CSS_SELECTOR, 'a.link-to-vehicle')[random_number] 
    random_vehicle.click()
    time.sleep(4)  # Wait for 3 seconds to see the changes

def logout(driver):
    """
    Logs out of the current account.

    Args:
        driver: The Selenium WebDriver instance.

    Returns:
        None
    """

    # Find the logout button element by its ID and click it
    logout_button = driver.find_element(By.ID, 'logout')
    logout_button.click()
    time.sleep(2) # Wait for 2 seconds