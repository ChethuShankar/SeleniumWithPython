import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))


class DragDrop():

    def handle_dragdrop(self):
        driver.get("https://jqueryui.com/droppable/")
        driver.maximize_window()
        driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@class='demo-frame']"))
        source=driver.find_element(By.ID,"draggable")
        target=driver.find_element(By.ID,"droppable")
        achains=ActionChains(driver)

        # drag and Dropwithout offset
        achains.drag_and_drop(source=source,target=target).perform() # Never forget perform() in the end
        time.sleep(4)
        achains.drag_and_drop_by_offset(source=source,xoffset=100,yoffset=100).perform()


dragdrop=DragDrop()
dragdrop.handle_dragdrop()


