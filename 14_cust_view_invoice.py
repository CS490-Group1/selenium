import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from datetime import datetime, timedelta
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import seleniumFunctions


driver = webdriver.Edge()
driver.get("http://localhost:3000/login")  # Open the website
driver.maximize_window()  # Open the browser in full screen
time.sleep(2)  # Wait for 2 seconds for the page to load

seleniumFunctions.log_into_existing_account(driver, 'customer@foyotahaven.com', 'Admin123')

driver.get("http://localhost:3000/myaccount")  # Open the website
time.sleep(3)  # Wait for 2 seconds for the page to load

payments_button = driver.find_element(By.NAME, 'myPayments')
payments_button.click()
time.sleep(7) #wait for things to load

random_number = random.randint(0, 3)
trans_option = Select(driver.find_element(By.NAME, 'transaction'))
trans_option.select_by_index(random_number)
time.sleep(3)

driver.quit()  # Close the browser
