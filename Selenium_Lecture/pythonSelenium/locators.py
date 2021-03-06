from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path='/Users/jonathan/study/TDD/Selenium_Lecture/chromedriver')
driver.get("https://rahulshettyacademy.com/angularpractice/")

# driver.find_element_by_name('name').send_keys('jinoh')
driver.find_element_by_css_selector('input[name="name"]').send_keys('jinoh')
driver.find_element_by_name('email').send_keys('jinoh')
driver.find_element_by_id('exampleCheck1').click()

# select class provide the methods to handle the options in dropdown
dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")

# xpath
driver.find_element_by_xpath("//input[@type='submit']").click()

message = driver.find_element_by_class_name("alert-success").text

assert "success" in message.lower()
driver.close()