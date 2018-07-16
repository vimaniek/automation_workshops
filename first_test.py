import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)

driver.get("http://demoqa.com/")
registration_button = driver.find_element_by_css_selector("#menu-item-374")
registration_button.click()

first_name_field = driver.find_element_by_css_selector("input[name = 'first_name']")
first_name_field.clear()
first_name_field.send_keys("Andrzej")

WebDriverWait(driver, 10).until(EC.visibility_of("input[name = 'last_name']"))
last_name_field = driver.find_element_by_css_selector("input[name = 'last_name']")
last_name_field.clear()
last_name_field.send_keys("Bot")

martial_status_radio_checkbox_list = driver.find_elements_by_css_selector("input[name = 'radio_4[]']")
martial_status_radio_checkbox_list[1].click()

hobby_checkbox_list = driver.find_elements_by_css_selector("input[name = 'checkbox_5[]']")
for element in hobby_checkbox_list:
    element.click()

country_dropdown_list = driver.find_elements_by_css_selector("#dropdown_7 > option")
country_dropdown_list[5].click()



time.sleep(10)
driver.close()
