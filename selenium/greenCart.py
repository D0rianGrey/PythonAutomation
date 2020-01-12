import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(10)
searchField = driver.find_element_by_xpath("//input[@class='search-keyword']")
searchField.send_keys("ber")
# time.sleep(5)
wait.until(expected_conditions.visibility_of_all_elements_located((By.XPATH, "//div[@class='product-action']/button")))

# foundResults = driver.find_elements_by_xpath("//div[@class='products']/div/h4")

addButtons = driver.find_elements_by_xpath("//div[@class='product-action']/button")

for i in addButtons:
    i.click()

driver.find_element_by_xpath("//a[@class='cart-icon']").click()
driver.find_element_by_xpath("//*[@id='root']/div/header/div/div[3]/div[2]/div[2]/button").click()
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()
print(driver.find_element_by_css_selector("span.promoInfo").text)
driver.quit()
