import time

from selenium import webdriver

from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.get("https://subscription.packtpub.com/")
time.sleep(10)


drive= driver.find_element(By.XPATH, '//*[@id="packt-navbar"]/a').rect
time.sleep(2)
# assert driver.find_element_by_css_selector("#element_id").value_of_css_property("color") == "rgb(0, 0, 255)"

# assert driver.find_element_by_css_selector("#element_id").location == {'x': 10, 'y': 20}
time.sleep(2)
driver.quit()
