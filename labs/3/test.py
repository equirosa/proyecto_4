from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://www.bnventadebienes.com/Home/HomeFilter")
time.sleep(10)
driver.quit()
print("Test completed")
