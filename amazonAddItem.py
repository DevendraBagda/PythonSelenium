from selenium import webdriver
import os

getCurrentDirectory = os.getcwd()
productUrl="https://www.amazon.in/Selenium-Python-Beginners-programming-language/dp/9389328810/ref=sr_1_2?keywords=python+selenium&qid=1579629190&sr=8-2"
driver=webdriver.Chrome(executable_path=getCurrentDirectory + '/chromedriver')
driver.maximize_window()
driver.get(productUrl)
driver.implicitly_wait(5)
driver.find_element_by_name('submit.add-to-cart').click()