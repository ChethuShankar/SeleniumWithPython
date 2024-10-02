import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from Base.base_driver import BaseDriver
from pages.search_result_page import ResultsPage
from utilities.utils import Utils


class HomePage(BaseDriver):
    log=Utils.custom_logger()
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.wait=wait

    def handle_push_button(self):
        # time.sleep(5)
        # if self.wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[@id='webpush-onsite']"))):
        # if self.wait_until_element_is_clickable(By.XPATH, "//div[@class='container']"):
        #     self.driver.find_element(By.XPATH, "//a[@class='close']").click()
        # time.sleep(10)
        # if self.wait_until_presence_of_elements(By.XPATH, "//iframe[@id='webpush-onsite']"):
        if self.driver.find_element(By.XPATH, "//iframe[@id='webpush-onsite']"):

            self.driver.switch_to.frame(self.driver.find_element(By.XPATH, "//iframe[@id='webpush-onsite']"))
            self.driver.find_element(By.XPATH, "//button[@class='button close']").click()
            self.driver.switch_to.default_content()


        else:
            pass

    # Locators
    Depart_from_locator = "//input[@id='BE_flight_origin_city']"
    Going_To_city_locator = "//input[@id='BE_flight_arrival_city']"
    Auto_suggestion_locator = "//div[@class='viewport']//div[1]//li"
    select_date_locator = "//input[@id='BE_flight_origin_date']"
    all_dates_locator = "//div[@id='monthWrapper']//tr//td[@class!='inActiveTD weekend']"
    Search_flight_button_locator = "//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']"

    def deprartfrom(self, departlocation):
        search = self.driver.find_element(By.XPATH, self.Depart_from_locator)

        search.click()

        search.send_keys(departlocation)

        search.send_keys(Keys.ENTER)

    def goingto(self, goingtoloctaion):
        going_to = self.driver.find_element(By.XPATH, self.Going_To_city_locator)
        going_to.click()
        going_to.send_keys(goingtoloctaion)

        search_results = self.driver.find_elements(By.XPATH, self.Auto_suggestion_locator)
        print(len(search_results))
        self.log.info(len(search_results))
        for results in search_results:
            if goingtoloctaion in results.text:
                results.click()
                break

    def select_date(self, departureDate):
        # self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_date']"))).click()
        self.wait_until_element_is_clickable(By.XPATH, self.select_date_locator).click()
        # all_dates = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='monthWrapper']//tr//td["
        #                                                                   "@class!='inActiveTD weekend']"))).find_elements(
        # By.XPATH, "//div[@id='monthWrapper']//tr//td[@class!='inActiveTD weekend']")
        all_dates = self.wait_until_element_is_clickable(By.XPATH, self.all_dates_locator).find_elements(
            By.XPATH, self.all_dates_locator)
        for i in all_dates:
            if i.get_attribute("data-date") == departureDate:
                i.click()
                # time.sleep(3)
                break

    def clicksearch_flight(self):
        self.driver.find_element(By.XPATH,
                                 self.Search_flight_button_locator).click()
        time.sleep(4)

    def POM_all_methods_Homepage(self, departlocation, goingtoloctaion, departureDate):
        self.handle_push_button()
        self.deprartfrom(departlocation)
        self.goingto(goingtoloctaion)
        self.select_date(departureDate)
        self.clicksearch_flight()

        # # Create a next page object here only to link between the pages and to reduce the multiplle object creation in the main file
        search_flight_results = ResultsPage(driver=self.driver)
        return search_flight_results
