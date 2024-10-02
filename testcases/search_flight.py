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



# driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))


class DemoExplicitWaits():

    @pytest.mark.usefixtures("setup")
    def explicit_waits_without_class_methods(self):
        # Launch Url



        #  Handle push notification
        if self.wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[@id='webpush-onsite']"))):

            self.driver.switch_to.frame(self.driver.find_element(By.XPATH, "//iframe[@id='webpush-onsite']"))
            self.driver.find_element(By.XPATH, "//button[@class='button close']").click()
            self.driver.switch_to.default_content()

            # Selecting source city

            search = self.driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")

            search.click()

            search.send_keys("New Delhi")

            search.send_keys(Keys.ENTER)

            #  Select destination city

            going_to = self.driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
            going_to.click()
            going_to.send_keys("Mum")

            search_results = self.driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]//li")
            print(len(search_results))
            for results in search_results:
                if "Mumbai (BOM)" in results.text:
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

            # select date

            all_dates = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='monthWrapper']//tr//td["
                                                                         "@class!='inActiveTD weekend']"))).find_elements(
                By.XPATH, "//div[@id='monthWrapper']//tr//td[@class!='inActiveTD weekend']")
            select_date = self.driver.find_elements(By.XPATH,
                                               "//div[@id='monthWrapper']//tr//td[@class!='inActiveTD weekend']")
            for i in all_dates:
                if i.get_attribute("data-date") == "30/08/2024":
                    i.click()
                    # time.sleep(3)
                    break

            # Click search flight button
            self.driver.find_element(By.XPATH,"//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']").click()
            time.sleep(4)

            #  Select filer 1 stop
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//p[normalize-space()='1']"))).click()

            # Scroll through the page
            pageLength = self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pageLength;")
            match = False
            while (match == False):
                lastCount = pageLength
                time.sleep(1)
                pageLength = self.driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pageLength;")
                if lastCount == pageLength:
                    match = True
            time.sleep(4)

            # Selecting all the searched results

            # all_1_stop_counts=driver.find_elements(By.XPATH,"(//span[contains(text(),'1 Stop')])")
            all_1_stop_counts=self.driver.find_elements(By.XPATH,"(//div[@class='flight-det full-width'])")

            #  Assertion:- checking 1 stop text is present in all lists
            for values in all_1_stop_counts:
                assert "1 Stop" in values.text
            print("assert passed")
            print(len(all_1_stop_counts))




