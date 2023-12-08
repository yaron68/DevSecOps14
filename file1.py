import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

search_word = sys.argv[1]
# Assuming you have already initialized your WebDriver (e.g., webdriver.Chrome())
driver = webdriver.Chrome()
url = "https://elbitsystemscareer.com/search-results/?keywords="
places = ['שרון' ,'גוש דן']
for place in places:
    driver.get(url)
    select_element = driver.find_element(By.ID, 'select')

    # Use the Select class to interact with the dropdown
    select = Select(select_element)

    select.select_by_visible_text(place)
    button = driver.find_element(By.XPATH, '//button[@aria-label="חפש לפי איזור"]')

    # Click the button
    button.click()
    end = True
    index = 1
    while(end):
        # Locate the text search_word" using XPath
        try:
            xpath_search = f"//label[a[contains(text(), '{search_word}')]]"
            job_description = driver.find_element(By.XPATH, xpath_search)
        except:
            # Locate the "הבא" link by its class name
            try:
                next_button = driver.find_element(By.CLASS_NAME, 'next')

                # Click the "הבא" link
                next_button.click()
                index += 1
                continue
            except:
                break
        # Get the text content of the label
        job_description_text = job_description.text
        print(f"aria {place} page {index} : {job_description_text}")
        try:
            next_button = driver.find_element(By.CLASS_NAME, 'next')

            # Click the "הבא" link
            next_button.click()
            index += 1
        except:
            break

# Close the browser window
driver.quit()
