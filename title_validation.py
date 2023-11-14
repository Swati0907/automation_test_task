from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://subscription.packtpub.com/")
main_title = driver.find_element(By.CLASS_NAME, 'text-white')
suggested_titles = driver.find_elements(By.CLASS_NAME, 'productCarousel')

max_iterations = 3
iteration_count = 0

for title in suggested_titles:
    txt = title.text
    print(f"Suggested Title {iteration_count + 1}: {txt}")

    title.click()
    time.sleep(20)

    updated_main_title_text = txt
    assert txt == updated_main_title_text, f"Test failed for title: {txt}"
    print(f"Test passed for Suggested Title {iteration_count + 1}: {txt}")

    iteration_count += 1
    if iteration_count >= max_iterations:
        break
