from login import authorize
from selenium.webdriver.support.ui import Select
from input_data import LOGIN, PASSWORD

driver = authorize(LOGIN, PASSWORD, 'https://avangard66.ru/wp-admin/edit.php?post_type=product')
driver.implicitly_wait(10)

products = driver.find_elements_by_class_name('row-title')
links = []
for p in products:
    links.append(p.get_property('href'))

for link in links[0:80]:
    driver.get(link)
    driver.implicitly_wait(10)
    selector = Select(driver.find_element_by_name("_woodmart_swatches_attribute"))
    selector.select_by_value("pa_czvet-yu-plast")

    driver.find_element_by_id('publish').click()