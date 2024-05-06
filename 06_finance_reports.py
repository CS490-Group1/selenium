import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import seleniumFunctions

email = "customer2"

driver = webdriver.Edge()
driver.get("http://localhost:3000/login")
driver.maximize_window()

time.sleep(2)

seleniumFunctions.log_into_existing_account(driver, 'manager@foyotahaven.com', 'Admin123')

manager_panel = driver.find_element(By.CSS_SELECTOR, '.hiddenPanels')
manager_panel.click()
time.sleep(5)

report_button = driver.find_element(By.NAME, 'reportsButton')
report_button.click()
time.sleep(2)


report_options = Select(driver.find_element(By.NAME,'customer'))
report_options.select_by_visible_text('Haley Mault - hmault0@nih.gov')
time.sleep(4)

report_options.select_by_visible_text('Ker Reichardt - kreichardt1@japanpost.jp')
time.sleep(2)

report_options.select_by_visible_text('Renault Hyam - rhyam4@army.mil')
time.sleep(4)

report_options.select_by_visible_text('Tanhya Antonomoli - tantonomolij@ovh.net')
time.sleep(2)



time.sleep(2)
driver.quit()  