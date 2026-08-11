# buy an item from a demo-site with Selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

# Login
wait = WebDriverWait(driver, 10)

username_field = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
username_field.send_keys("standard_user")

password_field = driver.find_element(By.ID, "password")
password_field.send_keys("secret_sauce")

login_button = driver.find_element(By.ID, "login-button")
login_button.click()
# input("✅")

wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))

first_product_add_button = driver.find_element(By.XPATH, "//div[@class='inventory_item'][1]//button")
first_product_add_button.click()

cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
cart_icon.click()

wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart_item")))
cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
assert len(cart_items) == 1, f"Expected 1 cart item, but got {len(cart_items)}"

# if len(cart_items) == 1:
#     print("Success!")
# else:
#     print("Failed!")

driver.quit()