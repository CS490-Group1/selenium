import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Edge()
driver.get("http://localhost:3000/login")  # Open the website
driver.maximize_window()  # Open the browser in full screen
time.sleep(2)  # Wait for 2 seconds for the page to load

# Click the 'Register' button to open the registration form
register_button = driver.find_element(By.CSS_SELECTOR, '.btn-modal')
register_button.click()
time.sleep(1)  # Wait for 1 second for the form to load

fname="Bob"
lname="Smith"

# Fill out the registration form
first_name = driver.find_element(By.ID, 'first_name')
first_name.send_keys(fname)
time.sleep(0.75)   

last_name = driver.find_element(By.ID, 'last_name')
last_name.send_keys(lname)
time.sleep(0.75)

dob = driver.find_element(By.ID, 'dob')
dob.send_keys('01/01/1995')
dob.send_keys(Keys.ESCAPE)
time.sleep(0.75)

email = driver.find_element(By.ID, 'email')
email.send_keys(f"{fname+lname}@gmail.com")
time.sleep(0.75)

password = driver.find_element(By.ID, 'password')
password.send_keys('Admin123')
time.sleep(0.75)

confirm_password = driver.find_element(By.ID, 'confirm_password')
confirm_password.send_keys('Admin123')
time.sleep(0.75)

drivers_license = driver.find_element(By.ID, 'drivers_license')
drivers_license.send_keys('123123123')
time.sleep(0.75)

phone = driver.find_element(By.ID, 'phone')
phone.send_keys('123-456-7890')
time.sleep(0.75)

# Click the 'Create New Account' button to submit the form
create_account_button = driver.find_element(By.CSS_SELECTOR, '.aws-btn')
create_account_button.click()

time.sleep(8)  # Wait for 5 seconds to see the changes
driver.quit()  # Close the browser
