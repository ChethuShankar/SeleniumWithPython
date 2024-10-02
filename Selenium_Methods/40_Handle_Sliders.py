import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))


class Slider():

    def handle_slider(self):
        driver.get("https://www.snapdeal.com/products/mobiles-cases-covers?sort=plrty")
        driver.maximize_window()
        left_slider=driver.find_element(By.XPATH,"//a[contains(@class,'left-handle')]")
        right_slider=driver.find_element(By.XPATH,"//a[contains(@class,'right-handle')]")
        #Method 1
        ActionChains(driver).drag_and_drop_by_offset(left_slider,30,0).perform()
        time.sleep(2)

        #Method 2
        ActionChains(driver).click_and_hold(left_slider).pause(1).move_by_offset(20,0).release().perform()
        time.sleep(4)

        #Method 3
        ActionChains(driver).move_to_element(left_slider).pause(1).click_and_hold(left_slider).move_by_offset(50,0).release().perform()
        time.sleep(4)

        #Method to slide right slider to left
        ActionChains(driver).drag_and_drop_by_offset(right_slider,-60,0).perform()
        time.sleep(2)

slider=Slider()
slider.handle_slider()