import time

import assertion as assertion
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By



# Load the page of TSO


driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.maximize_window()
wait = WebDriverWait(driver, 10)

base_url = "https://www.tsoatchampions.com/"
#driver.get(base_url)
# Do stuff before going to the site
#driver.set_page_load_timeout(10)
try:
    driver.get(base_url)
    print("Page loaded")
except TimeoutException:
    print("Failed to load the page:", driver.current_url)

assert "TSO-CHAMPIONS" in driver.title
#title not correct assertionerror shown

#accept the cookies of webpage
driver.find_element(By.XPATH,'//*[@id="accept-cookies"]').click()

#click the appointment page
driver.find_element(By.LINK_TEXT,"Book Your Appointment").click()
assert "TL-AMS" in driver.title
print("next page loaded")

#choose the admin login
button = driver.find_element(By.CSS_SELECTOR, "a[href='login']")

driver.execute_script("arguments[0].click();", button)

assert "Admin Login" in driver.title
print("Admin login page loaded")

driver.find_element(By.ID,"userName").send_keys("username")
driver.find_element(By.ID,"password").send_keys("password")
driver.find_element(By.XPATH,'/html/body/section/div/div[2]/div/div/form/div[3]/div/button').click()

#correct login details - successful shown
#incorrect login details - invalid credential shown
#print("invalid credentials")
print("successfully login")


time.sleep(80)
driver.close()

#Scenario 1: Enter your email address and password, then click the sign-in button.

#Result 1: No error message would be raised, thus letting execution continue successfully to the end.

#Scenario 2: Enter a valid username but incorrect values into the password field and click the sign-in button.

#Result 2: An invalid login error will be displayed, which will notify the user of entering junk characters into the password input fields.