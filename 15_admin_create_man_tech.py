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

seleniumFunctions.log_into_existing_account(driver, 'admin@foyotahaven.com', 'Admin123')

driver.get("http://localhost:3000/myaccount")  # Open the website
time.sleep(3)  # Wait for 2 seconds for the page to load

admin_panel_button = driver.find_element(By.NAME, 'admin')
admin_panel_button.click()
time.sleep(1) #wait for things to load

fname="Selenium"
lname="Manager"

# Fill out the registration form
first_name = driver.find_element(By.ID, 'man_first_name')
first_name.send_keys(fname)
time.sleep(0.75)   

last_name = driver.find_element(By.ID, 'man_last_name')
last_name.send_keys(lname)
time.sleep(0.75)

dob = driver.find_element(By.ID, 'man_dob')
dob.send_keys('01/01/1995')
dob.send_keys(Keys.ESCAPE)
time.sleep(0.75)

email = driver.find_element(By.ID, 'man_email')
email.send_keys(f"{fname+lname}@gmail.com")
time.sleep(0.75)

password = driver.find_element(By.ID, 'man_password')
password.send_keys('Admin123')
time.sleep(0.75)

confirm_password = driver.find_element(By.ID, 'man_confirm_password')
confirm_password.send_keys('Admin123')
time.sleep(0.75)

phone = driver.find_element(By.ID, 'man_phone')
phone.send_keys('123-456-7890')
time.sleep(0.75)

# Click the 'Create New Account' button to submit the form
create_man_button = driver.find_element(By.CSS_SELECTOR, '.registerBtn')
create_man_button.click()

time.sleep(8)  # Wait for 5 seconds to see the changes


driver.quit()  # Close the browser
