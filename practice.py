import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.edge.service import Service as EdgeService
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
#
# driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

# Firefox driver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# driver.get("https://www.facebook.com/")
# driver.find_element(By.XPATH, "//a[@data-testid='open-registration-form-button']").click()
# time.sleep(5)
# list = driver.find_elements(By.XPATH, "//select[@aria-label='Month']//child::option[@value]")
# for i in list:
#     print(i)
# print(values)
# values = driver.find_element(By.NAME, "firstname").get_attribute('aria-label')


# driver.get("https://www.yatra.com/hotels")
# time.sleep(2)
# driver.switch_to.frame(driver.find_element(By.ID,"webpush-onsite"))
# driver.find_element(By.ID,"deny").click()
# driver.switch_to.default_content()
# time.sleep(2)
# driver.find_element(By.XPATH,"//label[normalize-space()='Traveller and Hotel']").click()
# time.sleep(2)
# x=driver.find_element(By.XPATH,"//span[@class='pax-num-child adultcount']//following::span[@class='ddSpinnerPlus']").is_displayed()
# print(x)

from selenium.webdriver.support.select import Select
class Dropdown:
    def dropdown(self):

        driver.get("https://www.facebook.com/")
        driver.find_element(By.LINK_TEXT,"Create new account").click()
        time.sleep(2)
        dd=driver.find_element(By.XPATH,"//select[@aria-label='Month']")
        dropdown=Select(dd)
        dropdown.select_by_index(6)
        time.sleep(2)
        dropdown.select_by_value("2")
        time.sleep(2)
        dropdown.select_by_visible_text("Oct")

# obj=Dropdown()
# obj.dropdown()

class AutoSuggesion:
    def autosuggesion(self):
        driver.get("https://www.yatra.com/")
        time.sleep(3)
        # driver.switch_to.frame(driver.find_element(By.ID,"webpush-onsite"))
        # driver.find_element(By.ID,"deny").click()
        # driver.switch_to.default_content()

        search=driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_city']")
        search.click()
        search.screenshot(".\\elementscrnshot.png")
        search.send_keys("New")
        search.click()
        time.sleep(2)
        search_results=driver.find_elements(By.XPATH,"//div[@class='viewport']")
        for i in search_results:
            if "New York (JFK)" in i.text:
                i.click()
                break
                time.sleep(2)

        going_to=driver.find_element(By.XPATH,"//input[@id='BE_flight_arrival_city']")
        going_to.send_keys("Ba")
        search_result_2=driver.find_elements(By.XPATH,"//div[@class='ac_results dest_ac']//div[@class='viewport']")
        time.sleep(2)
        for resuts in search_result_2:
            if "Bangalore (BLR)" in resuts.text:
                resuts.click()
                time.sleep(2)
                break


        # calender
        # // div[@class ='month-wrapper'] // tr // td[@ class ='inActiveTD weekend']
        time.sleep(4)
        driver.find_element(By.ID,"BE_flight_origin_date").click()
        dates=driver.find_elements(By.XPATH,"// div[@class ='month-wrapper']//tr//td[@ class!='inActiveTD weekend']")
        for i in dates:
            if i.get_attribute("data-date")=="29/09/2024":
                i.click()
                time.sleep(2)
                break

        driver.get_screenshot_as_file(".\\screenshot_practice.png")





auto=AutoSuggesion()
auto.autosuggesion()


