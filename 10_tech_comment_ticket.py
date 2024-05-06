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

seleniumFunctions.log_into_existing_account(driver, 'tech@foyotahaven.com', 'Admin123')

driver.get("http://localhost:3000/myaccount")  # Open the website
time.sleep(3)  # Wait for 2 seconds for the page to load

tech_panel_button = driver.find_element(By.NAME, 'tech')
tech_panel_button.click()
time.sleep(7) #wait for things to load

# serviceAppointmentField
wait = WebDriverWait(driver, 10)
SA_submitted = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.serviceAppointmentField')))

hr = "09"
min = "00"
test_drive_date = datetime.now() + timedelta(days=3)
formatted_date = test_drive_date.strftime('%m%d%Y')
formatted_time = test_drive_date.strftime(f'{hr}{min}a')
saved_date = f"{test_drive_date.strftime('%a, %d %b %Y ')}{hr}:{min}:00 GMT"

for SA in SA_submitted:
    # print("car name: ",SA.text)
    if saved_date in SA.text:
        SA.click()
        time.sleep(3)
        break  

time.sleep(4)

service_comments = driver.find_element(By.CSS_SELECTOR, '.comment-input')
service_comments.clear()
service_comments.send_keys("Random Comment")

time.sleep(2) #show comment

save_button = driver.find_element(By.CSS_SELECTOR, '.service-appointments-save_update-button')
save_button.click()
time.sleep(4)  # Wait for 8 seconds to see the changes

driver.switch_to.alert.accept()

time.sleep(7) #wait for reload

wait = WebDriverWait(driver, 10)
SA_submitted = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.serviceAppointmentField')))

hr = "09"
min = "00"
test_drive_date = datetime.now() + timedelta(days=3)
formatted_date = test_drive_date.strftime('%m%d%Y')
formatted_time = test_drive_date.strftime(f'{hr}{min}a')
saved_date = f"{test_drive_date.strftime('%a, %d %b %Y ')}{hr}:{min}:00 GMT"

for SA in SA_submitted:
    # print("car name: ",SA.text)
    if saved_date in SA.text:
        SA.click()
        time.sleep(3)
        break  

time.sleep(4)

driver.quit()  # Close the browser
