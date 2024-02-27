from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.youtube.com/")
search = driver.find_element(By.NAME, "search_query")
search.click()
search.clear()
search.send_keys("Pantropiko by BINI")
search.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
