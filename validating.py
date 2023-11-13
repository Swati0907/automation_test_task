import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://subscription.packtpub.com/")
time.sleep(2)
try:
    browse_library = driver.find_element(By.XPATH, '//*[@id="packt-navbar"]/div[1]').rect
    packt_logo = driver.find_element(By.CLASS_NAME,'navbar-brand').rect
    search_field = driver.find_element(By.CLASS_NAME,'form-inline').rect
    cart = driver.find_element(By.CLASS_NAME,'btn-content').rect
    expected_browse_library_rect ={'height': 42, 'width': 111, 'x': 169.890625, 'y': 14}
    expected_packt_logo_rect = {'height': 36, 'width': 90, 'x': 55, 'y': 16.875}
    expected_search_field_rect = {'height': 40, 'width': 205, 'x': 480.921875, 'y': 15}
    expected_cart_rect = {'height': 40, 'width': 50, 'x': 912, 'y': 15}

    # actual_browse_library_color = browse_library.value_of_css_property('color')
    # expected_browse_library_color = "rgb(69, 74, 85)"
    actual_browse_library_txt = driver.find_element(By.XPATH, '//*[@id="packt-navbar"]/div[1]').text
    expected_browse_libray_txt= "Browse Library"

    assert browse_library == expected_browse_library_rect, "Browse Library  mismatch"
    assert packt_logo == expected_packt_logo_rect, "Packt Logo  mismatch"
    assert search_field == expected_search_field_rect, "Search field  mismatch"
    assert cart == expected_cart_rect, "Cart mismatch"
    assert actual_browse_library_txt == expected_browse_libray_txt, "Browse libray text mismatch"
    print("All assertions passed Successfully. Elements match expected values!")
except NoSuchElementException as e:
    print(f"Element not found: {e.msg}")
