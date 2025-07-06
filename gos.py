import requests
import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# List of proxies (you can add more as needed)
proxies_list = [
    "http://12.34.56.78:9999",
    "http://98.76.54.32:5000",
    "http://23.45.67.89:8088",
    "http://192.168.1.1:3128",
    "http://203.0.113.0:8080",
    "http://198.51.100.14:1080",
    "http://140.82.121.6:443",
    "http://55.23.11.88:80",
    "http://172.16.254.2:9090",
    "http://64.233.160.0:8888",
    "http://123.123.123.123:8000",
    "http://74.125.24.39:5555",
    "http://185.72.9.66:8888"
]

def get_proxy():
    """Fetch a random proxy from the list."""
    return random.choice(proxies_list)

def change_ip():
    """Change IP using a proxy."""
    proxy = get_proxy()
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Enable headless mode for Termux/CMD
    chrome_options.add_argument(f'--proxy-server={proxy}')
    return chrome_options

def create_facebook_account():
    """Automates Facebook account creation in headless mode."""
    chrome_options = change_ip()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.facebook.com/")

    # Manual Input Section via Termux/CMD
    name = input("Enter Full Name: ")
    birthday = input("Enter Birthday (MM/DD/YYYY): ")
    gender = input("Enter Gender (Male/Female): ")
    email = input("Enter Email: ")
    password = input("Enter Password: ")

    # Fill Form (Assuming field names)
    driver.find_element("name", "firstname").send_keys(name.split()[0])
    driver.find_element("name", "lastname").send_keys(name.split()[1])
    driver.find_element("name", "reg_email__").send_keys(email)
    driver.find_element("name", "reg_passwd__").send_keys(password)

    # Submit Form
    driver.find_element("name", "websubmit").click()

    # Verification Code Input via Termux/CMD
    code = input("Enter Verification Code: ")
    driver.find_element("name", "code").send_keys(code)
    driver.find_element("name", "confirm").click()

    print("Account Created Successfully!")
    driver.quit()

if __name__ == "__main__":
    create_facebook_account()
