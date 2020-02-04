from selenium import webdriver
import time
import math

from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    inputFirstName = browser.find_element_by_class_name("form-control.first")
    inputFirstName.send_keys("name")

    inputLastName = browser.find_element_by_class_name("form-control.second")
    inputLastName.send_keys("last name")

    inputEmail = browser.find_element_by_class_name("form-control.third")
    inputEmail.send_keys("e-mail")

    button = browser.find_element_by_class_name("btn.btn-default")
    button.click()
    time.sleep(1)

    welcomeText = browser.find_element_by_tag_name("h1").text

    assert "Congratulations!! You have successfully registered!" == welcomeText


finally:
    time.sleep(4)
    browser.quit()


