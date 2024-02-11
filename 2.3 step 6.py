from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element(By.CLASS_NAME, "trollface.btn-primary")
button.click()

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

input = browser.find_element(By.ID, "answer")
input.send_keys(y)

button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
button.click()

    # ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
    # закрываем браузер после всех манипуляций
browser.quit()