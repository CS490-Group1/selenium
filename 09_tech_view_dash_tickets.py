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
driver.get("http://localhost:3000/login")
seleniumFunctions.log_into_existing_account(driver, 'tech@foyotahaven.com', 'Admin123')

tech_panel = driver.find_element(By.CSS_SELECTOR, '.hiddenPanels')
tech_panel.click()
time.sleep(5)

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

close_modal = driver.find_element(By.CSS_SELECTOR, '.close-modal')
close_modal.click()


time.sleep(2)
driver.quit()
