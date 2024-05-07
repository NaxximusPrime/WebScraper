from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get("http://google.com")
assert "Google" in browser.title

# Find the search box
elem = browser.find_element(By.NAME, "p")

elem.send_keys("seleniumhq" + Keys.RETURN)

browser.quit()