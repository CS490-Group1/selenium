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

seleniumFunctions.log_into_existing_account(driver, 'manager@foyotahaven.com', 'Admin123')

driver.get("http://localhost:3000/myaccount")  # Open the website
time.sleep(3)  # Wait for 2 seconds for the page to load

man_panel_button = driver.find_element(By.NAME, 'manager')
man_panel_button.click()
time.sleep(7) #wait for things to load

reports_button = driver.find_element(By.NAME, 'reportsButton')
reports_button.click()
time.sleep(2)

# # Find all the vehicle elements by their CSS selector and click the random vehicle

month_option = Select(driver.find_element(By.NAME, 'selectMonth'))
month_option.select_by_visible_text('February')
time.sleep(1)

year_option = driver.find_element(By.ID, 'yearInput')
year_option.send_keys("2024")

time.sleep(4)

generate_button = driver.find_element(By.NAME, 'generateReportButton')
generate_button.click()
time.sleep(3)

driver.quit()  # Close the browser
