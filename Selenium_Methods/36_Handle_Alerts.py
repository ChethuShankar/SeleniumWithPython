import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

class Alerts():

    def handle_alerts(self):
        driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert")
        driver.maximize_window()
        driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='iframeResult']"))
        driver.find_element(By.XPATH,"//button[normalize-space()='Try it']").click()
        time.sleep(4)
        print(driver.switch_to.alert.text)
        driver.switch_to.alert.dismiss()




alerts=Alerts()
alerts.handle_alerts()