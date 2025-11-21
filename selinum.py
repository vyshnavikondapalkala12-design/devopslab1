from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Automatically install and manage ChromeDriver
service = Service(ChromeDriverManager().install())

# Set up Chrome WebDriver
driver = webdriver.Chrome(service=service)

try:
    # Step 1: Open Google
    driver.get("https://www.google.com")

    # Step 2: Find the search box
    search_box = driver.find_element(By.NAME, "q")

    # Step 3: Enter CMRCET website URL
    search_box.send_keys("https://cmrcet.ac.in/")
    search_box.send_keys(Keys.RETURN)

    # Step 4: Wait to see results
    time.sleep(200)

finally:
    # Step 5: Close the browser
    driver.quit()