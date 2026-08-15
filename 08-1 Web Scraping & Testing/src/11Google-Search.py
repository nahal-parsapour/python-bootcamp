from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://google.com")

search = driver.find_element("name", "q")
search.send_keys("Python developer roadmap")
search.send_keys(Keys.RETURN)

results = driver.find_elements("xpath", "//h3")
print(results[0].text)
driver.quit()