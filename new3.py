from selenium import webdriver
import time
import math
import os


link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
currentDir = os.path.abspath(os.path.dirname(__file__))
filePath = os.path.join(currentDir, 'test.txt')

print(os.path.abspath(os.path.dirname(__file__)))
print(filePath)

try:
    browser.get(link)
    browser.find_element_by_name("firstname").send_keys("firstname")
    browser.find_element_by_name("lastname").send_keys("lastname")
    browser.find_element_by_name("email").send_keys("email@email.mail")
    browser.find_element_by_id("file").send_keys(filePath)
    browser.find_element_by_class_name("btn.btn-primary").click()

finally:
    time.sleep(15)
    browser.quit()