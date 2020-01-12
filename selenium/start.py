from selenium import webdriver

# driver = webdriver.Chrome(executable_path="c:\\")
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()

# for cypress https://rahulshettyacademy.com/seleniumPractise/#/
# for java    https://rahulshettyacademy.com/AutomationPractice/
# for angular https://rahulshettyacademy.com/angularpractice/

# driver.get("https://www.rahulshettyacademy.com/#/index")
# print(driver.title)
# print(driver.current_url)
# driver.quit()

driver.get("https://rahulshettyacademy.com/angularpractice/")
dropDown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropDown.select_by_visible_text("Female")
getText = driver.find_element_by_id("exampleFormControlSelect1").text
print(getText)

#dropDown.select_by_index(0)



