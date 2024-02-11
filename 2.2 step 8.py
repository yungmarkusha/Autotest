from selenium import webdriver
browser = webdriver.Chrome()
from selenium.webdriver.common.by import By
import time
import os

browser = webdriver.Chrome()
link = "https://suninjuly.github.io/file_input.html"
browser.get(link)

input1 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Enter first name']")
input1.send_keys("Ivan")

input2 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Enter last name']")
input2.send_keys("Petrov")

input3 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Enter email']")
input3.send_keys("Petrov@mail.ru")

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'C:\ext.txt')           # добавляем к этому пути имя файла
element = browser.find_element(By.ID, "file")
element.send_keys(file_path)

button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
button.click()

    # ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(15)
    # закрываем браузер после всех манипуляций
browser.quit()