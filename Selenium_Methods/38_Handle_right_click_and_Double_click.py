import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

class RightClickDoubleClick():

    def handle_right_double_clicks(self):
        driver.get("https://demo.guru99.com/test/simple_context_menu.html")
        # driver.maximize_window()
        # Right click
        achains=ActionChains(driver)
        right_click_element=driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")
        time.sleep(2)
        achains.context_click(right_click_element).perform()
        time.sleep(2)
        copy_elem=driver.find_element(By.XPATH,"//span[normalize-space()='Copy']")
        copy_elem.click()
        print(driver.switch_to.alert.text)
        driver.switch_to.alert.accept()
        
        time.sleep(3)

        # Double click
        achains.double_click(driver.find_element(By.XPATH,"//button[normalize-space()='Double-Click Me To See Alert']")).perform()
        time.sleep(2)
        print(driver.switch_to.alert.text)



clicks=RightClickDoubleClick()
clicks.handle_right_double_clicks()

