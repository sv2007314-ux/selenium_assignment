from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://quotes.toscrape.com")
time.sleep(10)

input("press enter to close browser")
driver.close()