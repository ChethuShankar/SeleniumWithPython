import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

class ExecuteJavascript():
    def javascript(self):
        driver.execute_script("window.open('https://training.rcvacademy.com','_self');")
        time.sleep(8)
        driver.execute_script("window.open('https://training.revacademy.com/', 'self');")
        time.sleep(8)
        demo_element = driver.execute_script("return document.getElementsByTagName('p')[1];")
        driver.execute_script("arguments[0].click();", demo_element)




execute=ExecuteJavascript()
execute.javascript()