import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

class MouseOver():

    def handle_mouse_over(self):
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        # handle push notification
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='webpush-onsite']"))
        driver.find_element(By.XPATH, "//button[@class='button close']").click()
        driver.switch_to.default_content()

        # handle mouse over by ActionChains
        achain=ActionChains(driver)
        morebtn=driver.find_element(By.XPATH,"//span[@class='more-arr']")
        my_acc=driver.find_element(By.XPATH,"//a[contains(text(),'My Account')]")
        achain.move_to_element(my_acc).perform()
        driver.find_element(By.ID,"signInBtn").click()
        achain.move_to_element(morebtn).perform() # Never miss perform() in the end bcz action chain is incomplete without it
        time.sleep(4)
        # driver.find_element(By.XPATH,"//span[normalize-space()='Xplore']").click() # Not working


mouse_over=MouseOver()
mouse_over.handle_mouse_over()