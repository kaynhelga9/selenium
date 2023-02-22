from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

browser.get('https://techstepacademy.com/trial-of-the-stones')

#1
i1 = browser.find_element(By.ID, 'r1Input')
i1.send_keys('rock')
b1 = browser.find_element(By.ID, 'r1Btn')
b1.click()

#2
i2 = browser.find_element(By.ID, 'r2Input')
i2.send_keys(browser.find_element(By.ID, 'passwordBanner').find_element(By.TAG_NAME, 'h4').text)
b2 = browser.find_element(By.ID, 'r2Butn')
b2.click()

#3
m1 = browser.find_element(By.XPATH, '//b[text()="Jessica"]/../../p').text
m2 = browser.find_element(By.XPATH, '//b[text()="Bernard"]/../../p').text
res = 0
if int(m1) > int(m2): 
    res = 'Jessica'
else:
    res = 'Bernard'
i3 = browser.find_element(By.ID, 'r3Input')
i3.send_keys(res)
b3 = browser.find_element(By.ID, 'r3Butn')
b3.click()

#check
b4 = browser.find_element(By.ID, 'checkButn')
b4.click()

assert browser.find_element(By.XPATH, '//div[@id="trialCompleteBanner"]/h4').text == 'Trial Complete'

time.sleep(5)

