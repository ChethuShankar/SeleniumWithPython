import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

class MultipleWindows():

    def handle_multiple_windows(self):
        all_handle_list = []
        driver.get("https://www.yatra.com/")
        # driver.maximize_window()
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='webpush-onsite']"))
        driver.find_element(By.XPATH, "//button[@class='button close']").click()
        driver.switch_to.default_content()
        parent_handle=driver.current_window_handle
        print(f"current handle:- {parent_handle}")
        driver.find_element(By.XPATH,"//img[@alt='Flat 12% OFF (up to Rs. 1,800)']").click()
        all_handles=driver.window_handles
        print(all_handles)
        for handles in all_handles:
            if handles!=parent_handle:
                child_handle=handles
                driver.switch_to.window(handles) # chnging to child window
                driver.find_element(By.XPATH,"//span[normalize-space()='Luxury Trains']").click()
                driver.maximize_window()
                all_handles2=driver.window_handles
                for handle2 in all_handles2:
                    if handle2!=parent_handle and handle2!=child_handle:
                        driver.switch_to.window(handle2) # changing to grandchild window
                        time.sleep(3)
                        driver.find_element(By.XPATH,"//div[normalize-space()='MAHARAJA EXPRESS']").click()
                        latest_window=driver.window_handles[-1]
                        driver.switch_to.window(driver.window_handles[-1])
                        print("Successfully switched to maharaja express tab")
                        driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Chethan")
                        time.sleep(4)
                        driver.find_element(By.XPATH,"//button[@id='booknow-btn']").click()



                time.sleep(4)
                driver.close() # Here it will close the child tab
                break

        driver.switch_to.window(parent_handle)
        driver.find_element(By.XPATH, "//img[@class='conta iner']").click()
        time.sleep(2)

multiple_window=MultipleWindows()
multiple_window.handle_multiple_windows()