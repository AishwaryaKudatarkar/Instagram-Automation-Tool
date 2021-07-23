from selenium import webdriver 
import time

#sleep()->to prevent thrashing and throttingat servers.
browser=webdriver.Chrome("E:\Chrome_Driver\chromedriver.exe") #path of the chrome browser
browser.get("https://www.instagram.com/")
time.sleep(4)

#Login
Username=browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
Username.send_keys("__username__") #username
time.sleep(4)

Password=browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
Password.send_keys("__password__") #password
Password.submit()
time.sleep(6)

#Not now save password
NotNow=browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
time.sleep(4)
NotNow.click()
time.sleep(8)

#no notification
Noti=browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
time.sleep(4)
Noti.click()
time.sleep(2)

def story():
    time.sleep(4)
    s1=browser.find_element_by_xpath("/html/body/div[1]/section/main/section/div/div[1]/div/div/div/div/ul/li[3]/div/button/div[2]")
    time.sleep(4)
    s1.click()

story()