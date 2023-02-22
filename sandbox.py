from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import re

#config
options = Options()
options.add_experimental_option("detach", True) #prevent closing

#helpers
def printPage():
    print(browser.title, browser.current_url)
browser = webdriver.Chrome(options=options)

#main
browser.get("https://azurlane.koumakan.jp/wiki/Azur_Lane_Wiki")

targetParents = browser.find_elements(By.CLASS_NAME, "azl_news_title")
for p in targetParents: 
    if re.match(r".*ONGOING.*", p.text): 
        # print(p.text.encode('utf-8'))
        p.click()
        browser.implicitly_wait(2)


browser.quit()

