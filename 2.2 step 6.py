from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
link = "https://suninjuly.github.io/execute_script.html"
browser.get(link)

def calc(xx):
    return str(math.log(abs(12 * math.sin(int(xx)))))

x = browser.find_element(By.ID, "input_value")
xx = int(x.text)
y = calc(xx)

browser.execute_script("window.scrollBy(0, 100);")

input = browser.find_element(By.ID, "answer")
input.send_keys(y)

option1 = browser.find_element(By.ID, "robotCheckbox")
option1.click()

option2 = browser.find_element(By.ID, "robotsRule")
option2.click()

button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
button.click()

    # ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(15)
    # закрываем браузер после всех манипуляций
browser.quit()