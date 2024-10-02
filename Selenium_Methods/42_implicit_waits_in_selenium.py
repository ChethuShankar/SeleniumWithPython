import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))


class ImplicitWaits():  # Notes is in
    def implicit_waits(self):
        driver.get("https://www.facebook.com/signup")
        driver.maximize_window()
        driver.implicitly_wait(10)
        # driver.find_element(By.XPATH, "//input[@id='u_0_g_Wy']").send_keys("test@test.com")
        # driver.find_element(By.ID,'u_0_g_Wy').send_keys("chethan.shankar@gmail.com")

        #
        driver.find_element(By.NAME, 'reg_email__').send_keys("Chethan.shanka@gmail.com")
        driver.find_element(By.NAME, 'firstnam').send_keys("Chethan")
        # driver.find_element(By.CSS_SELECTOR,'#terms-link').click()
        # driver.find_element(By.LINK_TEXT,'Cookies Policy').click()


implicit_wait = ImplicitWaits()
implicit_wait.implicit_waits()
