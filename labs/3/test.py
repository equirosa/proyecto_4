from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.bnventadebienes.com/Home/HomeFilter")
provincia_select = driver.find_element(by=By.ID, value="ProvinceId")
provincia_select.click()
time.sleep(10)
driver.quit()
print("Test completed")
