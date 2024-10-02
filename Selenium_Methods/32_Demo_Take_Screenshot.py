import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

class DemoScreenshot(): # Video no 32:- How to ta
    def get_screenshot(self):
        driver.get("https://www.yatra.com/")
        driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='webpush-onsite']"))
        driver.find_element(By.XPATH, "//button[@class='button close']").click()
        driver.switch_to.default_content()

        # Click sign in button
        driver.find_element(By.XPATH,"//a[contains(text(),'My Account')]").click()
        loginbutton=driver.find_element(By.XPATH,"// a[ @ id = 'signInBtn']")
        loginbutton.click()
        time.sleep(3)
        continuebutton=driver.find_element(By.XPATH,"//button[@id='login-continue-btn']")
        continuebutton.screenshot(".\\test.png") # This will take screenshot of that particular element
        continuebutton.click()
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\Users\\Feelgood\\Documents\\get_screenshot.png")
        driver.save_screenshot(".\\save_screenshot_method.png")

demo_screenshot=DemoScreenshot()
demo_screenshot.get_screenshot()
