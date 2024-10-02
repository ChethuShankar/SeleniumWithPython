import logging

from selenium.webdriver.common.by import By

from Base.base_driver import BaseDriver
from selenium.webdriver.support import expected_conditions as EC

from utilities.utils import Utils


class ResultsPage(BaseDriver):
    log = Utils.custom_logger()
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
        # self.wait=wait

    Filter_By_non_Stop="//p[normalize-space()='0']"
    Filter_By_1_Stop = "//p[normalize-space()='1']"
    Filter_By_2_Stop = "//p[normalize-space()='2']"
    Search_flight_results="(//div[@class='flight-det full-width'])"

    # def select_filter_0_stop(self):
    #     self.wait_until_element_is_clickable(By.XPATH, self.Filter_By_0_Stop).click()


    def select_filter_0_stop(self):
        self.wait_until_element_is_clickable(By.XPATH, self.Filter_By_non_Stop).click()
    def select_filter_1_stop(self):
        # self.driver.refresh()
        self.wait_until_element_is_clickable(By.XPATH, self.Filter_By_1_Stop).click()
        self.log.info("1 Stop filter is selected")

    def select_filter_2_stop(self):
        # self.driver.refresh()
        self.wait_until_element_is_clickable(By.XPATH, self.Filter_By_2_Stop).click()

    def filter_by_0_stop(self):
        self.wait_until_element_is_clickable(By.XPATH,self.Filter_By_non_Stop).click()
    def filter_by_1_stop(self):
        # self.wait.until(EC.element_to_be_clickable((By.XPATH, "//p[normalize-space()='1']"))).click()
        # self.wait_until_element_is_clickable(By.XPATH, "//p[normalize-space()='1']").click()
        # all_1_stop_counts = self.wait.until(EC.presence_of_element_located((By.XPATH,"(//div[@class='flight-det full-width'])"))).find_elements(By.XPATH, "(//div[@class='flight-det full-width'])")

        self.select_filter_1_stop()

    def filter_by_2_stop_func(self):
        self.select_filter_2_stop()

    def get_flight_results(self):
        return self.wait_until_presence_of_elements(By.XPATH,self.Search_flight_results).find_elements(By.XPATH,self.Search_flight_results)


