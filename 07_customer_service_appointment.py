import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import seleniumFunctions
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta

email = "customer"
last="foyotahaven"

driver = webdriver.Edge()
driver.get("http://localhost:3000/services")
driver.maximize_window()
time.sleep(2)

login_to_service_vehicle = driver.find_element(By.NAME, 'login_for_services_button')
login_to_service_vehicle.click()
time.sleep(2)

seleniumFunctions.log_into_existing_account(driver, f'{email}@{last}.com', 'Admin123')

my_vehicles = driver.find_elements(By.NAME, 'select_vehicle_button_for_service')
print("MY VEHICLES:",len(my_vehicles))
if len(my_vehicles) == 1:
    my_vehicles[0].click()
else:
    random_number = random.randint(0, len(my_vehicles)-1)
    my_vehicles[random_number].click()
time.sleep(2)

add_services = driver.find_elements(By.CSS_SELECTOR, '.services-service')
random_number = random.randint(1, len(add_services)-1)
# print("RANDOM NUMBER:",random_number)
service = add_services[random_number].find_element(By.CSS_SELECTOR, '.add-button')
service.click()
time.sleep(2) 

accept_terms = driver.find_element(By.NAME, 'termsAccepted-services')
accept_terms.click()
time.sleep(2)

purchase_button = driver.find_element(By.NAME, 'make_appointment_button')
purchase_button.click()
time.sleep(2)  

# report_options = Select(driver.find_element(By.NAME,'customer'))
# report_options.select_by_visible_text('Haley Mault - hmault0@nih.gov')
# time.sleep(4)

locations = Select(driver.find_element(By.NAME,'city'))
locations.select_by_visible_text('Paterson')
time.sleep(4)

hr = "09"
min = "00"
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
schedule_service_appointment_button = driver.find_element(By.NAME, 'Schedule-Service-Appointment')
schedule_service_appointment_button.click()
time.sleep(3)

driver.switch_to.alert.accept()

driver.get("http://localhost:3000/myaccount")  # Open the website
time.sleep(3)  # Wait for 2 seconds for the page to load
# print(saved_date)

wait = WebDriverWait(driver, 10)
test_drives = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.serviceAppointmentField')))
# Iterate over the test drives
for test_drive in test_drives:
    # Get the date of the test drive
    test_drive_date = test_drive.find_element(By.CSS_SELECTOR, '.service_appointment_date').text

    # If the date of the test drive matches the saved date, click the test drive
    if test_drive_date == saved_date:
        test_drive.click()
        time.sleep(5)
        close_button = driver.find_element(By.CSS_SELECTOR, '.close-modal')
        close_button.click()
        break  # Exit the loop after clicking the matching test drive


time.sleep(2)
driver.quit()  

# print("RANDOM NUMBER:",random_number)
# print("MY VEHICLES:",len(my_vehicles))

# service_vehicle = driver.find_element(By.ID, 'service-vehicle-button')

# add_warranties = driver.find_elements(By.CSS_SELECTOR, '.service')
# random_number = random.randint(1, len(add_warranties)-1)
# print("RANDOM NUMBER:",random_number)
# warranty = add_warranties[random_number].find_element(By.CSS_SELECTOR, '.add-button')
# warranty.click()
# time.sleep(2) 
# accept_terms = driver.find_element(By.ID, 'termsAccepted-warranties')
# accept_terms.click()
# time.sleep(2)