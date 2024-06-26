import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 12 секунд, пока цена не станет равной 100

price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element([By.CSS_SELECTOR,'#price'], '100'))
option = browser.find_element(By.CSS_SELECTOR, '#book')
option.click()

num1 = browser.find_element(By.CSS_SELECTOR, '#input_value')
num1 = num1.text
y = calc(num1)

field = browser.find_element(By.CSS_SELECTOR, '#answer')
field.send_keys(y)

submit = browser.find_element(By.CSS_SELECTOR, "#solve")
submit.click()

time.sleep(5)
