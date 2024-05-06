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

# Find all the vehicle elements by their CSS selector and click the random vehicle
closable_appointment = driver.find_elements(By.CSS_SELECTOR, '.serviceAppointmentField')[0]
closable_appointment.click()
time.sleep(4)

service_comments = driver.find_element(By.CSS_SELECTOR, '.comment-input')
service_comments.clear()
service_comments.send_keys("Random Comment")

time.sleep(2) #show comment

status_option = Select(driver.find_element(By.NAME, 'change_Status'))
status_option.select_by_visible_text('Completed')
time.sleep(1)

save_button = driver.find_element(By.CSS_SELECTOR, '.service-appointments-save_update-button')
save_button.click()
time.sleep(4)  # Wait for 8 seconds to see the changes

driver.switch_to.alert.accept()

time.sleep(7) #wait for reload

driver.quit()  # Close the browser
