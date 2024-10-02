import time
import os
import softest

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

from pages.search_result_page import ResultsPage
from pages.yatra_home_page import HomePage
from utilities.utils import Utils
from ddt import ddt, data, unpack, file_data


# driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

@pytest.mark.usefixtures("setup")
@ddt
class Test_Search_Flight(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = HomePage(self.driver)
        self.assertion = Utils()

    # @data(("Bangalore","Mumbai","06/10/2024"),("Chennai","colombo","23/11/2024"))
    # @unpack

    # passing the test data from file(Json and Yaml)
    # json_path=os.path.join(os.getcwd(),'testcases','testdata','testdata.json')
    # @file_data(json_path)

    # passing data from excel file
    excel_json_path = os.path.join(os.getcwd(), 'testcases', 'testdata', 'tdataexcel.xlsx')

    # @data(*Utils.read_data_from_excel("D:\\Learnings\\Selenium_Framework\\testcases\\testdata\\tdataexcel.xlsx",
    #                                   "Sheet1")) # * is passed to ensure that list is being passed as inp
    # Passing data from csv file
    @data(*Utils.read_data_from_csv("D:\\Learnings\\Selenium_Framework\\testcases\\testdata\\tdatacsv.csv"))

    @unpack
    def test_search_flight(self, goingfrom, goingto, date):
        # Launch Url:- This is done by conftest,py page

        # Provide going from location

        # lp.handle_push_button() #This is to handle push button
        # lp.deprartfrom("Bangalore")
        #
        # # Provide going to location
        # lp.goingto("Chennai")
        #
        # # Select departure date
        # lp.select_date("06/09/2024")
        #
        # # Click Search flight button
        # lp.clicksearch_flight()

        # Doing all the operations at once
        search_flight_result = self.lp.POM_all_methods_Homepage(departlocation=goingfrom, goingtoloctaion=goingto,
                                                                departureDate=date)

        # search_flight_result = self.lp.POM_all_methods_Homepage(departlocation="Bangalore", goingtoloctaion="Mumbai",
        #                                                         departureDate="06/10/2024")

        # # Select 1 stop filter
        # sr = ResultsPage(self.driver)
        # sr.filter_by_1_stop()
        # all_1_stop_counts = sr.get_flight_results()

        # Scroll the page in search flight results page
        self.lp.page_scroll()

        # Select 1 stop filter --Just create a object inside yatra Homepage and call the method directly here
        # search_flight_result.filter_by_0_stop()
        search_flight_result.filter_by_1_stop()
        all_1_stop_counts = search_flight_result.get_flight_results()

        # # Scroll the page in search flight results page
        # lp.page_scroll()

        # assertions

        self.assertion.assertwithtext(all_1_stop_counts, "1 Stop")
