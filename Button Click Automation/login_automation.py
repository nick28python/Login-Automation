from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://-----.com//login")

username = driver.find_element(By.ID,"username")
password = driver.find_element(By.ID,"password")
login_button = driver.find_element(By.CLASS_NAME,"login_button")

username.send_keys("test_user")
password.send_keys("password123")
login_button.click()

time.sleep(5)
driver.quit()
