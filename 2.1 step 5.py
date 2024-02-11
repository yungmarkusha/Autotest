from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import math
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

answer_y = browser.find_element(By.ID, "answer")
answer_y.send_keys(y)

option1 = browser.find_element(By.ID, "robotCheckbox")
option1.click()

option2= browser.find_element(By.ID, "robotsRule")
option2.click()

button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
button.click()

    # ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
    # закрываем браузер после всех манипуляций
browser.quit()