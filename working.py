"""This is a file for testing only"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

driver.get("https://bandcamp.com/discover/")
#print(driver.title)
#driver.get("http://127.0.0.1")
driver.implicitly_wait(5)
print(f"\n{driver.title}\n")
html = driver.page_source
#print(html)

pagination_button = driver.find_element(By.ID, "view-more")
print(pagination_button.accessible_name)

tracks = driver.find_elements(By.CLASS_NAME, "results-grid-item")
print(len(tracks))
print(tracks[0].text)



driver.quit()


