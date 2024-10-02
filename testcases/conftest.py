import time
import os

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
driver=None


# def browser_setup(request,browser):
#     if browser == "edge":
#         driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
#     elif browser == "ff":
#         driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
#
#     driver.get("https://www.yatra.com/")
#     driver.maximize_window()
#     request.cls.driver = driver
#     yield
#     driver.close()
#
#
# def pytest_addoption(parser):
#     parser.addoption("--browser")
#
# @pytest.fixture(scope="class",autouse=True)
# def browser(request):
#     request.config.getoption("--browser")


@pytest.fixture(scope='class',autouse=True)
def setup(request,browser,url):
    # if browser=="ff":
    #     driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    # elif:
    #
    #     driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    # driver.get("https://www.yatra.com/")
    # # wait = WebDriverWait(driver, 10) #It's implemented in base_driver.py file
    # driver.maximize_window()
    # request.cls.driver = driver
    # # request.cls.wait=wait
    # yield
    # driver.close()

    global driver
    if browser == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    elif browser == "ff":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser=="chrome":
        driver= webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    else:
        # driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    #     # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

    # driver.get(url)
    driver.get("https://www.yatra.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")

@pytest.fixture(scope="class",autouse=True)
def browser(request):
    request.config.getoption("--browser")

@pytest.fixture(scope="class",autouse=True)
def url(request):
    request.config.getoption("--url")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
        extra.append(pytest_html.extras.url("http://www.yatra.com/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            report_directory = os.path.dirname(item.config.option.htmlpath)
            # file_name = str(int(round(time.time() * 1000))) + ".png"
            file_name = report.nodeid.replace("::", "_") + ".png"
            destinationFile = os.path.join(report_directory, file_name)
            driver.save_screenshot(destinationFile)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:300px;height=200px" ' \
                       'onclick="window.open(this.src)" align="right"/></div>'%file_name
            extra.append(pytest_html.extras.html(html))
        report.extra = extra

def pytest_html_report_title(report):
    report.title = "Automation Report"
