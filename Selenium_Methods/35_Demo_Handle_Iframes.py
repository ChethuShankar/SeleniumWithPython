import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

class Iframes():

    def handle_iframes(self):
        driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css")
        driver.maximize_window()
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='iframeResult']"))
        driver.switch_to.frame(1)
        time.sleep(4)
        driver.find_element(By.XPATH, "//a[text()='PYTHON']").click()
        time.sleep(4)
        driver.switch_to.default_content()


iframes=Iframes()
iframes.handle_iframes()