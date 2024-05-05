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
lman="Manager"

# Fill out the registration form
man_first_name = driver.find_element(By.ID, 'man_first_name')
man_first_name.send_keys(fname)
time.sleep(0.75)   

man_last_name = driver.find_element(By.ID, 'man_last_name')
man_last_name.send_keys(lman)
time.sleep(0.75)

man_dob = driver.find_element(By.ID, 'man_dob')
man_dob.send_keys('01/01/1995')
man_dob.send_keys(Keys.ESCAPE)
time.sleep(0.75)

man_email = driver.find_element(By.ID, 'man_email')
man_email.send_keys(f"{fname+lman}@gmail.com")
time.sleep(0.75)

man_password = driver.find_element(By.ID, 'man_password')
man_password.send_keys('Admin123')
time.sleep(0.75)

man_confirm_password = driver.find_element(By.ID, 'man_confirm_password')
man_confirm_password.send_keys('Admin123')
time.sleep(0.75)

man_phone = driver.find_element(By.ID, 'man_phone')
man_phone.send_keys('123-456-7890')
time.sleep(0.75)

# Click the 'Create New Account' button to submit the form
create_man_button = driver.find_element(By.CSS_SELECTOR, '.registerBtn')
create_man_button.click()

time.sleep(8)  # Wait for 5 seconds to see the changes

tech_first_name = driver.find_element(By.ID, 'tech_first_name')
tech_first_name.send_keys(fname)
time.sleep(0.75)   

ltech="Technician"
tech_last_name = driver.find_element(By.ID, 'tech_last_name')
tech_last_name.send_keys(ltech)
time.sleep(0.75)

tech_dob = driver.find_element(By.ID, 'tech_dob')
tech_dob.send_keys('01/01/1995')
tech_dob.send_keys(Keys.ESCAPE)
time.sleep(0.75)

tech_email = driver.find_element(By.ID, 'tech_email')
tech_email.send_keys(f"{fname+ltech}@gmail.com")
time.sleep(0.75)

tech_password = driver.find_element(By.ID, 'tech_password')
tech_password.send_keys('Admin123')
time.sleep(0.75)

tech_confirm_password = driver.find_element(By.ID, 'tech_confirm_password')
tech_confirm_password.send_keys('Admin123')
time.sleep(0.75)

tech_phone = driver.find_element(By.ID, 'tech_phone')
tech_phone.send_keys('123-456-7890')
time.sleep(0.75)

# Click the 'Create New Account' button to submit the form
create_tech_button = driver.find_element(By.NAME, 'techCreateButton')
create_tech_button.click()

time.sleep(8)  # Wait for 5 seconds to see the changes


driver.quit()  # Close the browser
