from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://www.bncr.fi.cr")
time.sleep(10)
driver.quit()
print("Test completed")
