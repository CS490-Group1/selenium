import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("http://localhost:3000/")  # Open the website
driver.maximize_window()  # Open the browser in full screen
time.sleep(2)  # Wait for 2 seconds for the page to load

'''
Info about driver.find_by: https://selenium-python.readthedocs.io/locating-elements.html
'''

def scroll_through_vehicles():
    time.sleep(2)
    # Scroll through the 'vehicles-div'
    scroll_script = """
    var vehiclesDiv = document.getElementById('vehicles-div');
    for (var i = 0; i < 10; i++) {
        if (vehiclesDiv.scrollTop >= vehiclesDiv.scrollHeight - vehiclesDiv.clientHeight) {
            break;
        }
        vehiclesDiv.scrollTop += 100;
        await new Promise(resolve => setTimeout(resolve, 300));
    }
    vehiclesDiv.scrollTop = 0;
    """
    driver.execute_script(scroll_script)
    time.sleep(1)

# Navigate to the /vehicles page
driver.get("http://localhost:3000/vehicles")
time.sleep(2)  # Wait for 2 seconds for the page to load

scroll_through_vehicles()

# Select 'SUV' in the 'Body Style' dropdown
body_style = Select(driver.find_element(By.NAME,'bodyStyleSelection'))
body_style.select_by_visible_text('SUV')
# time.sleep(1)
scroll_through_vehicles()

# Select 'FAV4' in the 'Model' dropdown
model = Select(driver.find_element(By.NAME,'modelSelection'))
model.select_by_visible_text('FAV4')
scroll_through_vehicles()

# Select 'Silver', 'Blue', 'Red' in the 'Exterior Color' dropdown
for color_choice in ['Silver', 'Blue', 'Red']:
    color = Select(driver.find_element(By.NAME,'colorSelection'))
    color.select_by_visible_text(color_choice)
    scroll_through_vehicles()
    color.deselect_by_visible_text(color_choice)


# Sort by 'Price'
sort = Select(driver.find_element(By.ID,'sort'))
sort.select_by_visible_text('Price')
# time.sleep(1)
scroll_through_vehicles()

time.sleep(5)  # Wait for 5 seconds to see the changes
driver.quit()  # Close the browser
