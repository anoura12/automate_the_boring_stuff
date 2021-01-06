from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#taking the email and message from the user
address = input("Enter the email id you want to send the message to - ")
sub = input("Enter the text you want to send - ")

#sets up the chrome browser and opens gmail
driver = webdriver.Chrome()
driver.get('https://www.google.com/gmail/') 

#gets the selector for the email textbox and asks the user for their email id 
userElem = driver.find_element_by_id('identifierId')
email = input("Enter your email address - ")
userElem.send_keys(email)

#finds selector of the "next" button and clicks it 
linkElem = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')
linkElem.click()

#finds selector of the password textbox and takes the password from the user
password = input("Enter your password - ")
passElem = driver.find_element_by_name('password')
passElem.send_keys(password)

#finds the selector for the "next" button and clicks it
elem = driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]')
elem.click()

#the program waits for 7 seconds so that the main inbox page loads and then continues to look for the next selector. 
#Otherwise it gives an error saying that it can't find the required selector.(as it tries to find it on the loading page.) 
driver.implicitly_wait(7)

#finds selector for the compose button and clicks it
compose = driver.find_element_by_class_name('z0')
compose.click()

#finds selector for the recipient textbox and writes the email address.
recipient = driver.find_element_by_name('to')
recipient.send_keys("address")

#finds selector for the subject textbox. Then it clicks tab to go to the main message box. 
#This was done because the id of the message textbox kept changing. 
#Clicking tab went directly to the box without having to find a specific selector for it. 
subject = driver.find_element_by_name('subjectbox')
Keys.TAB
subject.send_keys("sub") #message 

#finds selector for the "send" button and clicks it
send = driver.find_element_by_xpath('//*[@id=":87"]')
send.click()

#hence, an email is sent.