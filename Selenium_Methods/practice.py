import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

# # Firefox driver
# from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.firefox.service import Service as FirefoxService
#
# driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


class Multiple_windows:
    def multiplewindows(self):

        driver.get("https://www.yatra.com/")
        time.sleep(3)
        driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='webpush-onsite']"))
        driver.find_element(By.XPATH,"//button[@id='deny']").click()
        driver.switch_to.default_content()
        driver.find_element(By.XPATH,"//button[@class='btngdpr']").click()
        parent_handle=driver.current_window_handle
        driver.find_element(By.XPATH,"//a[@href='https://www.yatra.com/offer/details/icici-bank-offers']//div[@class='image-holder']//img[@alt='Flat 12% OFF (up to Rs. 1,800)']").click()
        all_handle=driver.window_handles
        print(all_handle)
        for handle in all_handle:
            if handle!=parent_handle:
                driver.switch_to.window(handle)
                print(handle)
                time.sleep(2)
                driver.find_element(By.XPATH,"//a[@id='booking_engine_luxury_trains']").click()
                driver.switch_to.window(driver.window_handles[-1])
                time.sleep(2)
                driver.find_element(By.XPATH,"//div[normalize-space()='MAHARAJA EXPRESS']").click()
                driver.switch_to.window(driver.window_handles[-1])
                time.sleep(2)
                driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Chethan")
                time.sleep(2)
                driver.switch_to.window(parent_handle)
                driver.find_element(By.XPATH,"//span[normalize-space()='Hotels']").click()
                time.sleep(2)


# mw=Multiple_windows()
# mw.multiplewindows()

class Alerts:
    def alerts(self):
        driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert")
        driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='iframeResult']"))
        driver.find_element(By.XPATH,"//button[normalize-space()='Try it']").click()
        time.sleep(4)
        print(driver.switch_to.alert.text)
        driver.switch_to.alert.dismiss()
        driver.close()


# alert=Alerts()
# alert.alerts()

from selenium.webdriver.common.action_chains import ActionChains
ac=ActionChains(driver)
class MouseHoverandRightClick:
    def double_click(self):
        ac=ActionChains(driver)
        driver.get("https://demo.guru99.com/test/simple_context_menu.html")
        time.sleep(2)
        # driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='webpush-onsite']"))
        # driver.find_element(By.XPATH, "//button[@class='button close']").click()
        # driver.switch_to.default_content()
        more_btn=driver.find_element(By.XPATH,"//span[@class='more-arr']")
        ac.move_to_element(more_btn).perform()
        time.sleep(2)
        ac.context_click(more_btn)



# mouse=MouseHoverandRightClick()
# mouse.double_click()

class Slider:
    def slider(self):
        driver.get("https://www.snapdeal.com/products/mobiles-cases-covers?sort=plrty")
        driver.maximize_window()
        time.sleep(2)
        left_slider=driver.find_element(By.XPATH,"//a[@class='price-slider-scroll left-handle ui-slider-handle ui-state-default ui-corner-all hashAdded']")
        right_slider=driver.find_element(By.XPATH,"//a[@class='price-slider-scroll right-handle ui-slider-handle ui-state-default ui-corner-all hashAdded']")

        # Method 1
        ac.drag_and_drop_by_offset(left_slider,xoffset=20,yoffset=0).perform()
        time.sleep(4)

        #Method 2
        ac.move_to_element(left_slider).pause(1).click_and_hold(left_slider).move_by_offset(30,0).release().perform()
        time.sleep(4)



#
# slider=Slider()
# slider.slider()


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Waits:
    def waits(self):
        driver.get("https://www.snapdeal.com/products/mobiles-cases-covers?sort=plrty")
        driver.maximize_window()
        driver.implicitly_wait(10)
        signin_btn=driver.find_element(By.XPATH,"//span[@class='accountUserName col-xs-12 reset-padding']")
        ac.move_to_element(signin_btn).perform()
        time.sleep(2)

        #Explicit waits
        wait=WebDriverWait(driver,10)
        # Fluent waits
        wait=WebDriverWait(driver,10,poll_frequency=5,ignored_exceptions=[])
        search_btn=wait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='inputValEnter']")))
        search_btn.click()
        search_btn.send_keys("Vivo T3")
        list=driver.find_elements(By.XPATH,"//ul[@class='suggestionList_menu']")
        for i in list:
            if "vivo t3x 5g back cover" in i.text:
                i.click()
                time.sleep(4)
                break



wiats=Waits()
wiats.waits()



