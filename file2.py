
# import requests
# aa = requests.get("https://api.chucknorris.io/jokes/random")
# print(aa.text.split("value")[1])
# bb = aa.next
from selenium import webdriver
# Replace 'https://example.com' with the URL you want to visit
url_to_visit = "https://api.chucknorris.io/jokes/random"
# Use the webdriver to open a browser (in this case, Chrome)
driver = webdriver.Chrome()
try:
    # Visit the URL
    driver.get(url_to_visit)

    # Wait for a while (you can adjust the time as needed)
    driver.implicitly_wait(5)
    joke_value = driver.execute_script("return JSON.parse(document.body.innerText).value")
    print(joke_value)

    # Refresh the page

    for index in range(5):
    # Wait for a while again (optional)
        driver.implicitly_wait(5)
        driver.refresh()

        updated_at = driver.execute_script(" return JSON.parse(document.body.innerText).updated_at")
        joke_value = driver.execute_script(" return JSON.parse(document.body.innerText).value")
        print(f"joke number {index} updated_at :{updated_at}:")
        print(joke_value)
        # print(refreshed_page_source)

finally:
    # Close the browser window
    driver.quit()



