import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import seleniumFunctions

email = "customer1"
back = "gmail"

driver = webdriver.Edge()
driver.get("http://localhost:3000/vehicles")
driver.maximize_window()
time.sleep(2)

seleniumFunctions.select_random_vehicle(driver)

login_to_purchase_vehicle = driver.find_element(By.ID, 'Login-to-purchase-vehicle')
login_to_purchase_vehicle.click()
time.sleep(2)

seleniumFunctions.log_into_existing_account(driver, f'{email}@{back}.com', 'Admin123')

finance_vehicle = driver.find_element(By.ID, 'finance-vehicle-button')
finance_vehicle.click()
time.sleep(2)

name_of_vehicle = driver.find_element(By.CSS_SELECTOR, '.service-info').text
name_of_vehicle = name_of_vehicle
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



application_income = driver.find_element(By.NAME, 'income')
application_income.send_keys("100000")

application_down_payment = driver.find_element(By.NAME, 'down_payment')
application_down_payment.send_keys("10000")

application_submit_button = driver.find_element(By.CSS_SELECTOR, '.aws-btn__wrapper')
application_submit_button.click()
time.sleep(2)

loan_approved_button = driver.find_element(By.CSS_SELECTOR, '.link-to-purchase')
loan_approved_button.click()
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
    print(name_of_vehicle, "-----", contract.text)
    if name_of_vehicle in contract.text:
        contract.click()
        time.sleep(5)

        close_button = driver.find_element(By.CSS_SELECTOR, '.close-modal')
        close_button.click()
        break  
time.sleep(2)

seleniumFunctions.logout(driver)

driver.get("http://localhost:3000/login")
time.sleep(2) 


seleniumFunctions.log_into_existing_account(driver, 'manager@foyotahaven.com', 'Admin123')


manager_panel = driver.find_element(By.CSS_SELECTOR, '.hiddenPanels')
manager_panel.click()
time.sleep(5)

wait = WebDriverWait(driver, 10)
contracts_submitted = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.pendingContractCar')))

for contract in contracts_submitted:
    print("car name: ",contract.text)
    if name_of_vehicle in contract.text:
        contract.click()
        time.sleep(2)
        
        sign_contract = driver.find_element(By.CSS_SELECTOR, '.aws-btn__wrapper')
        sign_contract.click()
        time.sleep(5)
        
        break  
time.sleep(2)

seleniumFunctions.logout(driver)

driver.get("http://localhost:3000/login") 
time.sleep(2)  

seleniumFunctions.log_into_existing_account(driver, f"{email}@{back}.com", "Admin123")

side_panel_options = driver.find_elements(By.CSS_SELECTOR, '.row')
for option in side_panel_options:
    if option.text == "My Contracts":
        option.click()
        break
time.sleep(2)

contracts_submitted = driver.find_elements(By.NAME, 'contract_details_approved')
for contract in contracts_submitted:
    print(name_of_vehicle, "-----", contract.text)
    if name_of_vehicle in contract.text:
        contract.click()
        time.sleep(5)

        sign_contract = driver.find_element(By.CSS_SELECTOR, '.aws-btn__wrapper')
        sign_contract.click()
        time.sleep(5)

        break  


payment_type_ach = driver.find_element(By.ID, 'achPaymentButton')
payment_type_ach.click()

bank = Select(driver.find_element(By.NAME,'company'))
bank.select_by_visible_text('Bank of America')

account_number = driver.find_element(By.NAME, 'account_number')
account_number.send_keys("123123123123")
time.sleep(2)

routing_number = driver.find_element(By.NAME, 'routing_number')
routing_number.send_keys("021200339")
time.sleep(2)

payment_submit = driver.find_element(By.CSS_SELECTOR, '.aws-btn__wrapper')
payment_submit.click()
time.sleep(4)

side_panel_options = driver.find_elements(By.CSS_SELECTOR, '.row')
for option in side_panel_options:
    if option.text == "My Vehicles":
        option.click()
        break
time.sleep(2)

time.sleep(4) 
driver.quit() 
