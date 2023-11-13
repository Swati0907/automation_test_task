import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://subscription.packtpub.com/")
time.sleep(2)

try:
    top_nav_options = driver.find_elements(By.XPATH, '//*[@id="packt-navbar"]')
    sub_option = driver.find_element(By.XPATH, '//*[@id="packt-navbar"]/div[1]')
    sub_option_text = sub_option.text
    sub_option.click()
    print(sub_option_text)
    expected_url = "https://subscription.packtpub.com/search"
    actual_url = driver.current_url

    assert actual_url== expected_url, f"Sub-option navigation failed for {sub_option_text}"
    print("Nav bar is redirecting to the correct pages")
except Exception as e:
    print(f"Test failed: {e}")
