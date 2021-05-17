
# from time import sleep
# from selenium import webdriver

# browser = webdriver.Firefox()

# browser.get('https://www.instagram.com/')

# sleep(5)

# browser.close()


from selenium import webdriver
import time

from selenium.webdriver.firefox.webdriver import WebDriver


browser = WebDriver.get('https://www.instagram.com/')



time.sleep(5)



