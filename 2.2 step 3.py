from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

x = browser.find_element(By.ID, "num1")
num11 = x.text
y = browser.find_element(By.ID, "num2")
num22 = y.text
summa = int(num11) + int(num22)

select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(str(summa))

button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
button.click()



    # ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
    # закрываем браузер после всех манипуляций
browser.quit()