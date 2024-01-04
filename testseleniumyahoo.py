from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Initialize the Chrome WebDriver
s = Service('D:\Selenium\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=s)

# Open Yahoo
driver.get("http://www.yahoo.com")

# Find the search box element and enter a query
search_box = driver.find_element(By.ID, "ybar-sbq")
search_box.send_keys("NPRU")

# Find the search button and click it
btn_search = driver.find_element(By.ID, "ybar-search")
btn_search.click()

# Wait for the search results to load
time.sleep(5)

# Print the title of the current page
print(driver.title)

# Close the browser
driver.quit()
