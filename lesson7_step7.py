import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_treasure = browser.find_element(By.CSS_SELECTOR, '#treasure')
    treasure = x_treasure.get_attribute("valuex")
    y = calc(treasure)
    option1 = browser.find_element(By.CSS_SELECTOR, '#answer')
    option1.send_keys(y)

    option2 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option2.click()

    option3 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option3.click()

    option4 = browser.find_element(By.CSS_SELECTOR, ".btn")
    option4.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()