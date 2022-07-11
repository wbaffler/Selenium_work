import time
from selenium import webdriver

def authorize(USER, PASSWORD, LINK):
    driver = webdriver.Firefox()
    driver.get(LINK)
    driver.implicitly_wait(10)

    login = driver.find_element_by_id('user_login')
    password = driver.find_element_by_id('user_pass')
    login_button = driver.find_element_by_id('wp-submit')

    login.send_keys(USER)
    password.send_keys(PASSWORD)
    login_button.click()
    return driver
