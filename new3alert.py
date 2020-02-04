from selenium import webdriver
import time
import math
import os


link = "http://suninjuly.github.io/redirect_accept.html"

browser = webdriver.Chrome()
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser.get(link)
    browser.find_element_by_class_name("trollface.btn.btn-primary").click()
    browser.switch_to.window(browser.window_handles[1])
    browser.find_element_by_id("answer").send_keys(calc(browser.find_element_by_id("input_value").text))
    browser.find_element_by_class_name("btn.btn-primary").click()




finally:
    time.sleep(10)
    browser.close()