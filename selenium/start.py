from selenium import webdriver

# driver = webdriver.Chrome(executable_path="c:\\")

driver = webdriver.Chrome()
driver.maximize_window()
# https://rahulshettyacademy.com/AutomationPractice/
driver.get("https://www.rahulshettyacademy.com/#/index")
print(driver.title)
print(driver.current_url)
driver.quit()
