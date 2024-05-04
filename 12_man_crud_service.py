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

service_button = driver.find_element(By.NAME, 'serviceCenterButton')
service_button.click()
time.sleep(7)

# # Find all the vehicle elements by their CSS selector and click the random vehicle
random_number = random.randint(0, 4)
service = driver.find_elements(By.CSS_SELECTOR, '.serviceAppointmentField')[random_number]
service.click()
time.sleep(4)

service_cost = driver.find_element(By.NAME, 'serviceCost')
service_cost.clear()
time.sleep(1)
service_cost.send_keys("420.00")

time.sleep(2) #show comment

save_button = driver.find_element(By.NAME, 'saveServiceButton')
save_button.click()
time.sleep(1)

driver.switch_to.alert.accept()

time.sleep(7) #wait for reload

add_button = driver.find_element(By.NAME, 'addServiceButton')
add_button.click()

service_name = driver.find_element(By.NAME, 'serviceName')
service_name.send_keys("Selenium Testing")
time.sleep(1)
service_descrip = driver.find_element(By.NAME, 'serviceDescription')
service_descrip.send_keys("Most important type of testing")
time.sleep(1)
new_service_cost = driver.find_element(By.NAME, 'serviceCost')
new_service_cost.send_keys("999.99")
time.sleep(1)
service_img = driver.find_element(By.NAME, 'serviceIMG')
service_img.send_keys("https://i.imgur.com/yFkezWw.jpeg")
time.sleep(1)

new_service_button = driver.find_element(By.NAME, 'newServiceSaveButton')
new_service_button.click()
time.sleep(1)

driver.switch_to.alert.accept()
time.sleep(5)

driver.quit()  # Close the browser
