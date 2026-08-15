
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

text_input = driver.find_element("name", "my-text")
text_input.send_keys("Nahal Test")

submit = driver.find_element("css selector", "button")
submit.click()

driver.quit()