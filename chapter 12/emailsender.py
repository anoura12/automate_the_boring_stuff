from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
chrome_options = Options()

chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-setuid-sandbox")
 
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://www.google.com/gmail/')

userElem = driver.find_element_by_id('identifierId')
email = input("Enter your email address - ")
userElem.send_keys(email)
linkElem = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')
linkElem.click()
password = input("Enter your password - ")
passElem = driver.find_element_by_name('password')
passElem.send_keys(password)
elem = driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]')
elem.click()
driver.implicitly_wait(7)
compose = driver.find_element_by_xpath('//*[@id=":3c"]/div/div')
compose.click()
recipient = driver.find_element_by_name('to')
recipient.send_keys("ramesh.suja@gmail.com")
subject = driver.find_element_by_name('subjectbox')
Keys.TAB
subject.send_keys("Hello. This is the Matrix.")

send = driver.find_element_by_xpath('//*[@id=":87"]')
send.click()


#<button class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc qIypjc TrZEUc" jscontroller="soHxf" jsaction="click:cOuCgd; mousedown:UX7yZ; mouseup:lbsD7e; mouseenter:tfO1Yc; mouseleave:JywGue; touchstart:p6p2H; touchmove:FwuNnf; touchend:yfqBxc; touchcancel:JMtRjd; focus:AHmuwe; blur:O22p3e; contextmenu:mg9Pef;" jsname="LgbsSe" type="button"><div class="VfPpkd-Jh9lGc"></div><span jsname="V67aGc" class="VfPpkd-vQzf8d">Next</span><div class="VfPpkd-RLmnJb"></div></button>

#identifierNext > div > button