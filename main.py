from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

browser.get('https://techstepacademy.com/training-ground')

input_element = browser.find_element(By.ID, "ipt2")

button_element = browser.find_element(By.XPATH, "//button[@id='b4']")

input_element.send_keys('test')

button_element.click()

time.sleep(5)