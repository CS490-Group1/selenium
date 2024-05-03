import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("http://localhost:3000/vehicles")  # Open the website
driver.maximize_window()  # Open the browser in full screen
time.sleep(2)  # Wait for 2 seconds for the page to load


# Select 'Truck' in the 'Body Style' dropdown
body_style = Select(driver.find_element(By.NAME,'bodyStyleSelection'))
body_style.select_by_visible_text('Truck')
time.sleep(1)

# Select 'Fundra' in the 'Model' dropdown
model = Select(driver.find_element(By.NAME,'modelSelection'))
model.select_by_visible_text('Fundra')
time.sleep(1)

# Sort by 'Price'
sort = Select(driver.find_element(By.ID,'sort'))
sort.select_by_visible_text('Price')
time.sleep(1)

first_vehicle = driver.find_element(By.CSS_SELECTOR, 'a.link-to-vehicle')
first_vehicle.click()
time.sleep(3)  # Wait for 3 seconds to see the changes

time.sleep(5)  # Wait for 5 seconds to see the changes
driver.quit()  # Close the browser
