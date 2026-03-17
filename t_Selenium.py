from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://www.google.com")
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium")
search_box.submit()
time.sleep(10)
results = driver.find_elements(By.CSS_SELECTOR, "h3")
for result in results:
    print(result.text)
driver.quit()
time.sleep(10)