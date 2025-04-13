# 🔐 Login Automation using Selenium

A simple yet powerful Python automation script that logs into a website using Selenium WebDriver.  
Ideal for automating login flows, testing credentials, or creating login-based bots.

---

## 🚀 Features

- Automates login form submission
- Works on websites with standard form-based authentication
- Easily customizable for different login pages
- Clean and beginner-friendly code

---

## 🛠️ Tech Stack

- Python
- Selenium
- Chrome WebDriver

---

## 📋 How It Works

1. Opens the browser and navigates to the login page.
2. Locates the username, password fields, and login button using:
   - `ID` for username and password
   - `CLASS_NAME` for the login button
3. Fills in credentials and clicks login.
4. Waits 5 seconds before closing the browser.

---

## 💻 Sample Code

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://example.com/login")

username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.CLASS_NAME, "login_button")

username.send_keys("test_user")
password.send_keys("password123")
login_button.click()

time.sleep(5)
driver.quit()
