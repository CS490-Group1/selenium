import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import random
from datetime import datetime, timedelta
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import seleniumFunctions


driver = webdriver.Edge()
driver.get("http://localhost:3000/login")  # Open the website
driver.maximize_window()  # Open the browser in full screen
time.sleep(2)  # Wait for 2 seconds for the page to load

seleniumFunctions.log_into_existing_account(driver, 'customer@foyotahaven.com', 'Admin123')

driver.get("http://localhost:3000/vehicles")  # Open the website
time.sleep(3)  # Wait for 2 seconds for the page to load

seleniumFunctions.select_random_vehicle(driver)

# Select 'Paterson' in the 'city' dropdown
city = Select(driver.find_element(By.NAME,'city'))
city.select_by_visible_text('Paterson')
time.sleep(1)

hr = "09"
min = "08"
test_drive_date = datetime.now() + timedelta(days=3)
formatted_date = test_drive_date.strftime('%m%d%Y')
formatted_time = test_drive_date.strftime(f'{hr}{min}a')
saved_date = f"{test_drive_date.strftime('%a, %d %b %Y ')}{hr}:{min}:00 GMT"

date_time = driver.find_element(By.NAME, 'dateTime')
date_time.send_keys(formatted_date)
time.sleep(1)
date_time.send_keys(Keys.ARROW_RIGHT)
date_time.send_keys(formatted_time)
time.sleep(1)


# Click the 'Schedule Test Drive' button to submit the form
schedule_test_drive_button = driver.find_element(By.ID, 'Schedule-Test-Drive')
schedule_test_drive_button.click()
time.sleep(3)

# Press the Enter/Return key to dismiss the alert
driver.switch_to.alert.accept()

driver.get("http://localhost:3000/myaccount")  # Open the website
time.sleep(3)  # Wait for 2 seconds for the page to load
# print(saved_date)

# Get all the test drives
wait = WebDriverWait(driver, 10)
test_drives = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.testDriveField')))
# Iterate over the test drives
for test_drive in test_drives:
    # Get the date of the test drive
    test_drive_date = test_drive.find_element(By.CSS_SELECTOR, '.test_drive_date').text

    # If the date of the test drive matches the saved date, click the test drive
    if test_drive_date == saved_date:
        test_drive.click()
        time.sleep(5)
        close_button = driver.find_element(By.CSS_SELECTOR, '.close-modal')
        close_button.click()
        break  # Exit the loop after clicking the matching test drive

log_out_button = driver.find_element(By.ID, 'logout')
log_out_button.click()

driver.get("http://localhost:3000/login")  # Open the website
time.sleep(2)  # Wait for 2 seconds for the page to load

seleniumFunctions.log_into_existing_account(driver, 'manager@foyotahaven.com', 'Admin123')

manager_panel = driver.find_element(By.CSS_SELECTOR, '.hiddenPanels')
manager_panel.click()
time.sleep(5)
# Wait for the testDriveField elements to load
wait = WebDriverWait(driver, 10)
test_drives = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.testDriveField')))

for test_drive in test_drives:
    # Get the date of the test drive
    test_drive_date = test_drive.find_element(By.CSS_SELECTOR, '.test_drive_date').text

    # If the date of the test drive matches the saved date, click the test drive
    if test_drive_date == saved_date:
        test_drive.click()
        time.sleep(5)

        approve_button = driver.find_element(By.CSS_SELECTOR, '.approveOrDenyButtons')
        approve_button.click()

        time.sleep(5)

        break  # Exit the loop after clicking the matching test drive

log_out_button = driver.find_element(By.ID, 'logout')
log_out_button.click()

driver.get("http://localhost:3000/login")  # Open the website
time.sleep(2)  # Wait for 2 seconds for the page to load


seleniumFunctions.log_into_existing_account(driver, 'customer@foyotahaven.com', 'Admin123')

driver.get("http://localhost:3000/myaccount")  # Open the website
time.sleep(3)  # Wait for 2 seconds for the page to load

# Get all the test drives
wait = WebDriverWait(driver, 10)
test_drives = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.testDriveField')))
# Iterate over the test drives
for test_drive in test_drives:
    # Get the date of the test drive
    test_drive_date = test_drive.find_element(By.CSS_SELECTOR, '.test_drive_date').text

    # If the date of the test drive matches the saved date, click the test drive
    if test_drive_date == saved_date:
        test_drive.click()
        time.sleep(5)
        close_button = driver.find_element(By.CSS_SELECTOR, '.close-modal')
        close_button.click()
        break  # Exit the loop after clicking the matching test drive

time.sleep(4)  # Wait for 8 seconds to see the changes
driver.quit()  # Close the browser
