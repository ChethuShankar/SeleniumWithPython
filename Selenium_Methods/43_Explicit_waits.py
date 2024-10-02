import time
import pytest
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Imports for explicit waits
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))


class DemoExplicitWaits():
    def __init__(self):
        self.driver = driver
        # self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(driver, 20)
        self.url = "https://www.yatra.com/"

        # try:
        #     # self.wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@id='webpush-onsite']")))
        #     if (self.wait.until(EC.element_to_be_clickable((By.XPATH, "//iframe[@id='webpush-onsite']"))) or self.wait.until(EC.element_to_be_clickable((By.XPATH, "//iframe[@id='webpush-onsite']")))):
        #
        #         self.check_push_button = True
        #
        #     else:
        #         self.check_push_button = True
        # except TimeoutException as e:
        #     # self.check_push_button = False
        #     print("Iframe not found", (e))

    def handle_push_button(self):
        if self.wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[@id='webpush-onsite']"))):

            driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='webpush-onsite']"))
            driver.find_element(By.XPATH, "//button[@class='button close']").click()
            driver.switch_to.default_content()

        else:
            pass


    def actions(self):
        search = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")

        search.click()

        search.send_keys("New Delhi")

        search.send_keys(Keys.ENTER)
        going_to = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        going_to.click()
        going_to.send_keys("New")

        search_results = driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]//li")
        print(len(search_results))
        for results in search_results:
            if "New York (JFK)" in results.text:
                results.click()
                break

        #         Handle calenders in selenium
        #         Method 1:- Select date directly by hardcoding
        #         departure_date=driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_date']")
        #         departure_date.click()
        #         time.sleep(3)
        #         driver.find_element(By.XPATH,"//td[@id='09/07/2025']").click()
        #         time.sleep(2)

        #         Method 2:- Select date Dynamically and add explicit wait
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_date']"))).click()
        # departure_date = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']")
        # departure_date.click()
        all_dates = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='monthWrapper']//tr//td["
                                                                          "@class!='inActiveTD weekend']"))).find_elements(
            By.XPATH, "//div[@id='monthWrapper']//tr//td[@class!='inActiveTD weekend']")
        select_date = driver.find_elements(By.XPATH, "//div[@id='monthWrapper']//tr//td[@class!='inActiveTD weekend']")
        for i in all_dates:
            if i.get_attribute("data-date") == "25/08/2024":
                i.click()
                time.sleep(3)
                break

    def explicit_waits(self):
        # driver.get("https://www.yatra.com/")

        driver.get(self.url)
        driver.maximize_window()
        print(self.url)

        self.handle_push_button()
        self.actions()

        # if self.check_push_button:
        #     self.handle_push_button()
        #     self.actions()
        # else:
        #     self.actions()



    def explicit_waits_without_class_methods(self):
        driver.get("https://www.yatra.com/")
        wait = WebDriverWait(driver, 10)
        driver.maximize_window()
        driver.implicitly_wait(10)
        if wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[@id='webpush-onsite']"))):

            driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='webpush-onsite']"))
            driver.find_element(By.XPATH, "//button[@class='button close']").click()
            driver.switch_to.default_content()

            search = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")

            search.click()

            search.send_keys("New Delhi")

            search.send_keys(Keys.ENTER)
            going_to = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
            going_to.click()
            going_to.send_keys("New")

            search_results = driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]//li")
            print(len(search_results))
            for results in search_results:
                if "New York (JFK)" in results.text:
                    results.click()
                    break

            #         Handle calenders in selenium
            #         Method 1:- Select date directly by hardcoding
            #         departure_date=driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_date']")
            #         departure_date.click()
            #         time.sleep(3)
            #         driver.find_element(By.XPATH,"//td[@id='09/07/2025']").click()
            #         time.sleep(2)

            #         Method 2:- Select date Dynamically and add explicit wait
            wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_date']"))).click()
            # departure_date = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']")
            # departure_date.click()
            all_dates = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='monthWrapper']//tr//td["
                                                                              "@class!='inActiveTD weekend']"))).find_elements(
                By.XPATH, "//div[@id='monthWrapper']//tr//td[@class!='inActiveTD weekend']")
            select_date = driver.find_elements(By.XPATH,
                                               "//div[@id='monthWrapper']//tr//td[@class!='inActiveTD weekend']")
            for i in all_dates:
                if i.get_attribute("data-date") == "25/08/2024":
                    i.click()
                    # time.sleep(3)
                    break

        else:
            search = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")

            search.click()

            search.send_keys("New Delhi")

            search.send_keys(Keys.ENTER)
            going_to = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
            going_to.click()
            going_to.send_keys("New")

            search_results = driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]//li")
            print(len(search_results))
            for results in search_results:
                if "New York (JFK)" in results.text:
                    results.click()
                    break

            #         Handle calenders in selenium
            #         Method 1:- Select date directly by hardcoding
            #         departure_date=driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_date']")
            #         departure_date.click()
            #         time.sleep(3)
            #         driver.find_element(By.XPATH,"//td[@id='09/07/2025']").click()
            #         time.sleep(2)

            #         Method 2:- Select date Dynamically and add explicit wait
            wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_date']"))).click()
            # departure_date = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']")
            # departure_date.click()
            all_dates = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='monthWrapper']//tr//td["
                                                                              "@class!='inActiveTD weekend']"))).find_elements(
                By.XPATH, "//div[@id='monthWrapper']//tr//td[@class!='inActiveTD weekend']")
            select_date = driver.find_elements(By.XPATH,
                                               "//div[@id='monthWrapper']//tr//td[@class!='inActiveTD weekend']")
            for i in all_dates:
                if i.get_attribute("data-date") == "25/08/2024":
                    i.click()
                    # time.sleep(3)
                    break


demo_explicitwaits = DemoExplicitWaits()
# demo_explicitwaits.explicit_waits_without_class_methods()
demo_explicitwaits.explicit_waits()