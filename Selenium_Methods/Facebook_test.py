import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

# # Firefox imports
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.firefox import GeckoDriverManager
# driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))





class FindElement():
    def find_element_by_id(self):
        driver.get("https://www.facebook.com/signup")
        driver.maximize_window()
        time.sleep(4)
        # driver.find_element(By.XPATH, "//input[@id='u_0_g_Wy']").send_keys("test@test.com")
        # driver.find_element(By.ID,'u_0_g_Wy').send_keys("chethan.shankar@gmail.com")

        #
        driver.find_element(By.NAME,'reg_email__').send_keys("Chethan.shanka@gmail.com")
        driver.find_element(By.NAME, 'firstname').send_keys("Chethan")
        # driver.find_element(By.CSS_SELECTOR,'#terms-link').click()
        # driver.find_element(By.LINK_TEXT,'Cookies Policy').click()
        time.sleep(4)
        # driver.find_element(By.PARTIAL_LINK_TEXT,'Already have an acco').click()

#         Find_elements function gives all the count of elements present fpr the given By method
        lista=driver.find_elements(By.XPATH,"//select[@aria-label='Month']//child::option")
        for i in lista:
            print(i.text)
        print(len(lista))


class BrowserOperations():
    def browser_operations(self):
        driver.get("https://training.rcvacademy.com/") # to open the url
        print(driver.current_url) # To print the current url
        print(driver.title) # to print present page title
        driver.maximize_window() # to maximize the window and the windows menu will not dissappeared
        driver.fullscreen_window() #  it'll make the web page full screen
        driver.find_element(By.LINK_TEXT,"ALL COURSES").click()
        time.sleep(2)
        driver.refresh() # to refresh the current web page
        # Fills the entire screen, similar to pressing F11 in most browsers.
        driver.back() # go back to previous web page it's like press <-- button in browser
        time.sleep(2)
        driver.forward() # Going forward or press --> button in left corner
        time.sleep(2)
        driver.quit() # It'll quit all the web pages opened for the above driver
# Browser commands
# browser_action=BrowserOperations()
# browser_action.browser_operations()


# By_Id = FindElement()
# By_Id.find_element_by_id()



# Get elements by attribute
class GetAtrribute():
    def get_element_value_by_attribute(self):
        driver.get("https://training.rcvacademy.com/")
        driver.find_element(By.LINK_TEXT, "ALL COURSES").click()
        time.sleep(2)
        course_list=driver.find_elements(By.XPATH,"//select[@name='categories']//child::option").get_attribute("value")
        # for i in course_list:
        #     print(i.v)
        #     # i.__getattribute__("value")

        print(f"course list: {course_list}")
        driver.close() # close the current window
# attr_obj=GetAtrribute()
# attr_obj.get_element_value_by_attribute()


# Check whether Some button is enabled or not
class CheckButtonEnabled():
    def check_button(self):
        driver.get("https://training.openspan.com/login")
        button=driver.find_element(By.XPATH,"//input[@id='login_button']").is_enabled()
        print(button) # it'll print true if button is enabled else false
        driver.find_element(By.XPATH,"//input[@id='user_name']").send_keys("Chethan")
        driver.find_element(By.XPATH,"//input[@id='user_pass']").send_keys("Chethan123")
        button2=driver.find_element(By.XPATH,"//input[@id='login_button']").is_enabled()
        print(button2)
        

# button_check=CheckButtonEnabled()
# button_check.check_button()

# How to handle Hidden Elements in Selenium

class HiddenElement(): # Video 25
    def hidden_element_w3schools(self):
        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
        elem=driver.find_element(By.XPATH,"//div[@id='myDIV']").is_displayed()
        print(elem)
        driver.find_element(By.XPATH,"//button[normalize-space()='Toggle Hide and Show']").click()
        elem1=driver.find_element(By.XPATH,"//div[@id='myDIV']").is_displayed()
        print(elem1)
    def hidden_element_yatra(self):
        driver.get("https://www.yatra.com/")
        driver.find_element(By.XPATH,"//span[@class='demo-icon icon-hotels']").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"//label[normalize-space()='Traveller and Hotel']").click()
        time.sleep(2)
        # Switch to iframe by locators( This is to handle push notification popup)
        driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='webpush-onsite']"))
        print("Iframe switched using locators")

        # # Switch the frame by ID to handle push notifications (Not working)
        # driver.switch_to.frame("webpush-onsite")
        # print("Swiched using Id")
        #
        # # Switch Frame- By name
        # driver.switch_to.frame("webpush-onsite") # Same like id bcz both id and name is same for this frame
        driver.find_element(By.XPATH, "//button[@class='button close']").click()
        #  Switch back to default content
        driver.switch_to.default_content()
        time.sleep(2)
        driver.find_element(By.XPATH,"//span[@class='pax-num-child adultcount']//following::span[@class='ddSpinnerPlus']").click()
        time.sleep(2)

        elem2=driver.find_element(By.XPATH,"//select[@class='ageselect']").is_displayed()
        print(elem2) # It should print true or false




# hidden_obj=HiddenElement()
# hidden_obj.hidden_element_w3schools()
# hidden_obj.hidden_element_yatra()

class HandleCheckBox():
    def handle_checkbox(self):
        driver.get("https://www.yatra.com/flights")
        driver.maximize_window()
        driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='webpush-onsite']"))
        driver.find_element(By.XPATH,"//button[@class='button close']").click()
        driver.switch_to.default_content()
        driver.find_element(By.XPATH,"//a[normalize-space()='Non Stop Flights']").click()
        time.sleep(4)
        # Check whether the checkbox is selected or not
        if(driver.find_element(By.XPATH,"//a[normalize-space()='Non Stop Flights']//child::i[@class='ico ico-checkbox ico-checkbox-checked']").is_displayed()):
            print("Checkbox selected")
            driver.find_element(By.XPATH, "//a[normalize-space()='Non Stop Flights']").click()
            print("Initially selected and now unselected")
        else:
            print("Checkbox not selected")
        var1=driver.find_element(By.XPATH, "//a[normalize-space()='Non Stop Flights']").is_selected()
        print(var1)
        time.sleep(2)
        var2=driver.find_element(By.XPATH,"//a[normalize-space()='Student Fare']").is_selected()
        print(var2)
        driver.close()



# Handle_checkbox=HandleCheckBox()
# Handle_checkbox.handle_checkbox()

class Demo_RadioButton():
    def radio_button(self):
        driver.get("http://test.rubywatir.com/radios.php")
        driver.maximize_window()
        time.sleep(2)
        print(driver.find_element(By.XPATH, "//input[@value='Radio1']").is_selected())
        driver.find_element(By.XPATH, "//input[@value='Radio1']").click()
        print(driver.find_element(By.XPATH, "//input[@value='Radio1']").is_selected())




# Radio_button=Demo_RadioButton()
# Radio_button.radio_button()
from selenium.webdriver.support.select import Select
class DemoDropDownList():
    def dropdownlist(self):
        driver.get("https://www.facebook.com/signup")
        driver.maximize_window()
        dropdown=driver.find_element(By.XPATH,"//select[@id='month']")
        dd=Select(dropdown)
        dd.select_by_index(6)
        time.sleep(3)
        dd.select_by_value("1")
        time.sleep(3)
        dd.select_by_visible_text("Feb")
        time.sleep(3)

# Dropdown=DemoDropDownList()
# Dropdown.dropdownlist() # Same method for multiselect dropdown list

class DemoAutoSuggestion():
    def auto_suggestion(self):
        driver.get("https://www.yatra.com/")
        driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='webpush-onsite']"))
        driver.find_element(By.XPATH, "//button[@class='button close']").click()
        driver.switch_to.default_content()
        search=driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_city']")
        time.sleep(2)
        search.click()
        time.sleep(2)
        search.send_keys("New Delhi")
        time.sleep(2)
        search.send_keys(Keys.ENTER)
        going_to=driver.find_element(By.XPATH,"//input[@id='BE_flight_arrival_city']")
        going_to.click()
        going_to.send_keys("New")
        time.sleep(4)
        search_results=driver.find_elements(By.XPATH,"//div[@class='viewport']//div[1]//li")
        print(len(search_results))
        for results in search_results:
            if "New York (JFK)" in results.text:
                results.click()
                break
                time.sleep(4)

#         Handle calenders in selenium
#         Method 1:- Select date directly by hardcoding
        departure_date=driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_date']")
        departure_date.click()
        time.sleep(3)
        driver.find_element(By.XPATH,"//td[@id='09/07/2025']").click()
        time.sleep(2)

#         Method 2:- Select date Dynamically
        departure_date = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']")
        departure_date.click()
        time.sleep(3)
        select_date=driver.find_elements(By.XPATH,"//div[@id='monthWrapper']//tr//td[@class!='inActiveTD weekend']")
        for i in select_date:
            if i.get_attribute("data-date")=="25/08/2024":
                i.click()
                time.sleep(3)
                break




demo_autosuggestion=DemoAutoSuggestion()
demo_autosuggestion.auto_suggestion()


