from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.lambdatest.com")
first_form_input = driver.find_element_by_tag_name("input")

first_form_input.send_keys("emailid@lambdatest.com")

button = driver.find_element_by_link_text("Start Free Testing")
button.click()