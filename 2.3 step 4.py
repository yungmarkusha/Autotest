from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
button.click()

confirm = browser.switch_to.alert
confirm.accept()

def calc(xx):
    return str(math.log(abs(12 * math.sin(int(xx)))))
x = browser.find_element(By.ID, "input_value")
xx = int(x.text)
y = calc(xx)

input = browser.find_element(By.ID, "answer")
input.send_keys(y)

button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
button.click()
    # ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
    # закрываем браузер после всех манипуляций
browser.quit()