import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(
    executable_path=r'C:/Users/18326/Downloads/chromedriver_win32/chromedriver.exe', options=chrome_options)
for i in range(10):
    driver.get('http://www.google.com')

    search = driver.find_element_by_name('q')
    search.send_keys("teach 2 learn")
    search.send_keys(Keys.RETURN)  # hit return after you enter search text
    time.sleep(3)  # sleep for 5 seconds so you can see the results
    assert "No results found." not in driver.page_source
    driver.find_element_by_xpath(
        "//a[@href='https://www.weteach2learn.com/']").click()
    time.sleep(1)
    driver.quit()
