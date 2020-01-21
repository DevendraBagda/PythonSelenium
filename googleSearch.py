# importing required module
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os

getCurrentDirectory = os.getcwd()
# setting chrome driver
browser = webdriver.Chrome(executable_path=getCurrentDirectory + '/chromedriver')
# passing url for automation
browser.get('http://www.google.com')
#search the element by using element name
search = browser.find_element_by_name('q')
# give desire input
search.send_keys("My first selenium script")
# hit return after you enter search text
search.send_keys(Keys.RETURN) 
# sleep for 5 seconds so you can see the results
time.sleep(5)
# close the browser, when automation completed
browser.quit()
print('Automation Successfully completed...')