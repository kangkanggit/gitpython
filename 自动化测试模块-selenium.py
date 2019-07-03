from time import sleep

from selenium import webdriver

chrome = webdriver.Chrome()
chrome.get("https://www.baidu.com/")
inputs = chrome.find_element_by_id("kw")
inputs.send_keys("五塔山")
button = chrome.find_element_by_id("su")
button.click()
sleep(2)
chrome.close()