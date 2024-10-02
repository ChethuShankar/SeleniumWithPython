from selenium import webdriver

# Get imports from https://pypi.org/project/webdriver-manager/
# Edge selenium webdriver manager imports
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

# Firefox imports
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.firefox import GeckoDriverManager
#
# driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://www.facebook.com/signup")
driver.maximize_window()
print(driver.title)
