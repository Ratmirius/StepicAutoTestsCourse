from selenium import webdriver
import time
import math
link = "http://suninjuly.github.io/execute_script.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)


    valuex = browser.find_element_by_id("input_value").text
    print(valuex)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(calc(valuex))

    submitButton = browser.find_element_by_class_name("btn.btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submitButton)




    checkBox = browser.find_element_by_id("robotCheckbox")
    checkBox.click()
    radioButtonRobots = browser.find_element_by_id("robotsRule")
    radioButtonRobots.click()
    submitButton.click()





finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()