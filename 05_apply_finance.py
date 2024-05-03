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
driver.get("http://localhost:3000/vehicles")  # Open the website
driver.maximize_window()  # Open the browser in full screen
time.sleep(2)  # Wait for 2 seconds for the page to load

seleniumFunctions.select_random_vehicle(driver)

login_to_purchase_vehicle = driver.find_element(By.ID, 'Login-to-purchase-vehicle')
login_to_purchase_vehicle.click()
time.sleep(2)  # Wait for 2 second for the form to load

seleniumFunctions.log_into_existing_account(driver, 'customer@foyotahaven.com', 'Admin123')

finance_vehicle = driver.find_element(By.ID, 'finance-vehicle-button')
finance_vehicle.click()
time.sleep(2)  # Wait for 2 second for the form to load

name_of_vehicle = driver.find_element(By.CSS_SELECTOR, '.service-info').text
name_of_vehicle = name_of_vehicle.split()
name_of_vehicle = f"{name_of_vehicle[0]} {name_of_vehicle[3]} {name_of_vehicle[1]} {name_of_vehicle[2]}"
print(name_of_vehicle)

add_warranties = driver.find_elements(By.CSS_SELECTOR, '.service')
random_number = random.randint(1, len(add_warranties)-1)
print("RANDOM NUMBER:",random_number)
warranty = add_warranties[random_number].find_element(By.CSS_SELECTOR, '.add-button')
warranty.click()
time.sleep(2) 
accept_terms = driver.find_element(By.ID, 'termsAccepted-warranties')
accept_terms.click()
time.sleep(2)

purchase_button = driver.find_element(By.CSS_SELECTOR, '.link-to-purchase')
purchase_button.click()
time.sleep(2)  

application_name = driver.find_element(By.NAME, 'name')
application_name.send_keys("Bob")

application_income = driver.find_element(By.NAME, 'income')
application_income.send_keys("100000")

application_down_payment = driver.find_element(By.NAME, 'down_payment')
application_down_payment.send_keys("10000")

application_submit_button = driver.find_element(By.ID, 'submit-loan-application')
application_submit_button.click()
time.sleep(2)

loan_approved_button = driver.find_element(By.CSS_SELECTOR, '.link-to-purchase')
loan_approved_button.click()
time.sleep(2)  

buyer_name = driver.find_element(By.NAME, 'buyer_name')
buyer_name.send_keys("Bob")
time.sleep(2)

buyer_signature = driver.find_element(By.NAME, 'buyer_signature')
buyer_signature.send_keys("Bob")
time.sleep(2)

submit_contract = driver.find_element(By.CSS_SELECTOR, '.form-input-submit')
submit_contract.click()
time.sleep(2)

driver.switch_to.alert.accept()
time.sleep(2)

side_panel_options = driver.find_elements(By.CSS_SELECTOR, '.row')
for option in side_panel_options:
    if option.text == "My Contracts":
        option.click()
        break
time.sleep(2)

contracts_submitted = driver.find_elements(By.CSS_SELECTOR, '.contract_Details')
for contract in contracts_submitted:
    print("----",contract.text)
    print("////",contract.text.split("\n"))
    print("====",name_of_vehicle in contract.text.split("\n"))

    if name_of_vehicle in contract.text.split("\n"):
        print("FOUND")
        contract.click()
        break


# # Iterate over the test drives
# for warranty in add_warranties:
#     # Get the date of the test drive
#     warranty_info = warranty.find_element(By.CSS_SELECTOR, '.add-button').text

#     print(warranty_info)
    # # If the date of the test drive matches the saved date, click the test drive
    # if test_drive_date == saved_date:
    #     test_drive.click()
    #     time.sleep(5)
    #     close_button = driver.find_element(By.CSS_SELECTOR, '.close-modal')
    #     close_button.click()
    #     break  # Exit the loop after clicking the matching test drive

# driver.get("http://localhost:3000/vehicles")  # Open the website
# time.sleep(3)  # Wait for 2 seconds for the page to load


# # Select 'Paterson' in the 'city' dropdown
# city = Select(driver.find_element(By.NAME,'city'))
# city.select_by_visible_text('Paterson')
# time.sleep(1)

# hr = "09"
# min = "11"
# test_drive_date = datetime.now() + timedelta(days=3)
# formatted_date = test_drive_date.strftime('%m%d%Y')
# formatted_time = test_drive_date.strftime(f'{hr}{min}a')
# saved_date = f"{test_drive_date.strftime('%a, %d %b %Y ')}{hr}:{min}:00 GMT"

# date_time = driver.find_element(By.NAME, 'dateTime')
# date_time.send_keys(formatted_date)
# time.sleep(1)
# date_time.send_keys(Keys.ARROW_RIGHT)
# date_time.send_keys(formatted_time)
# time.sleep(1)


# # Click the 'Schedule Test Drive' button to submit the form
# schedule_test_drive_button = driver.find_element(By.ID, 'Schedule-Test-Drive')
# schedule_test_drive_button.click()
# time.sleep(3)

# # Press the Enter/Return key to dismiss the alert
# driver.switch_to.alert.accept()

# driver.get("http://localhost:3000/myaccount")  # Open the website
# time.sleep(3)  # Wait for 2 seconds for the page to load
# # print(saved_date)

# # Get all the test drives
# wait = WebDriverWait(driver, 10)
# test_drives = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.testDriveField')))
# # Iterate over the test drives
# for test_drive in test_drives:
#     # Get the date of the test drive
#     test_drive_date = test_drive.find_element(By.CSS_SELECTOR, '.test_drive_date').text

#     # If the date of the test drive matches the saved date, click the test drive
#     if test_drive_date == saved_date:
#         test_drive.click()
#         time.sleep(5)
#         close_button = driver.find_element(By.CSS_SELECTOR, '.close-modal')
#         close_button.click()
#         break  # Exit the loop after clicking the matching test drive

# log_out_button = driver.find_element(By.ID, 'logout')
# log_out_button.click()

# driver.get("http://localhost:3000/login")  # Open the website
# time.sleep(2)  # Wait for 2 seconds for the page to load

# login_button = driver.find_element(By.ID, 'log-in')
# login_button.click()
# time.sleep(1)  # Wait for 1 second for the form to load

# # Fill out the login form
# email = driver.find_element(By.ID, 'email')
# email.send_keys('manager@foyotahaven.com')
# time.sleep(0.75)

# password = driver.find_element(By.ID, 'password')
# password.send_keys('Admin123')
# time.sleep(0.75)

# # Click the 'Log In' button to submit the form
# login_button = driver.find_element(By.CSS_SELECTOR, '.aws-btn.aws-btn--primary.aws-btn--visible.false.aws-btn--progress')
# login_button.click()
# time.sleep(4)

# manager_panel = driver.find_element(By.CSS_SELECTOR, '.hiddenPanels')
# manager_panel.click()
# time.sleep(5)
# # Wait for the testDriveField elements to load
# wait = WebDriverWait(driver, 10)
# test_drives = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.testDriveField')))

# for test_drive in test_drives:
#     # Get the date of the test drive
#     test_drive_date = test_drive.find_element(By.CSS_SELECTOR, '.test_drive_date').text

#     # If the date of the test drive matches the saved date, click the test drive
#     if test_drive_date == saved_date:
#         test_drive.click()
#         time.sleep(5)

#         approve_button = driver.find_element(By.CSS_SELECTOR, '.approveOrDenyButtons')
#         approve_button.click()

#         time.sleep(5)

#         # close_button = driver.find_element(By.CSS_SELECTOR, '.close-modal')
#         # close_button.click()

#         break  # Exit the loop after clicking the matching test drive

# log_out_button = driver.find_element(By.ID, 'logout')
# log_out_button.click()

# driver.get("http://localhost:3000/login")  # Open the website
# time.sleep(2)  # Wait for 2 seconds for the page to load


# login_button = driver.find_element(By.ID, 'log-in')
# login_button.click()
# time.sleep(1)  # Wait for 1 second for the form to load

# # Fill out the login form
# email = driver.find_element(By.ID, 'email')
# email.send_keys('customer@foyotahaven.com')
# time.sleep(0.75)

# password = driver.find_element(By.ID, 'password')
# password.send_keys('Admin123')
# time.sleep(0.75)

# # Click the 'Log In' button to submit the form
# login_button = driver.find_element(By.CSS_SELECTOR, '.aws-btn.aws-btn--primary.aws-btn--visible.false.aws-btn--progress')
# login_button.click()
# time.sleep(4)

# driver.get("http://localhost:3000/myaccount")  # Open the website
# time.sleep(3)  # Wait for 2 seconds for the page to load

# # Get all the test drives
# wait = WebDriverWait(driver, 10)
# test_drives = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.testDriveField')))
# # Iterate over the test drives
# for test_drive in test_drives:
#     # Get the date of the test drive
#     test_drive_date = test_drive.find_element(By.CSS_SELECTOR, '.test_drive_date').text

#     # If the date of the test drive matches the saved date, click the test drive
#     if test_drive_date == saved_date:
#         test_drive.click()
#         time.sleep(5)
#         close_button = driver.find_element(By.CSS_SELECTOR, '.close-modal')
#         close_button.click()
#         break  # Exit the loop after clicking the matching test drive

time.sleep(4)  # Wait for 8 seconds to see the changes
driver.quit()  # Close the browser
