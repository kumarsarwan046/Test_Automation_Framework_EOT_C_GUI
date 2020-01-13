import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from utils import Utils
from pages.loginpage import LoginPage
from pages.Anomaly_keyword_Management import Anomaly_management
class Test(unittest.TestCase):
    def test(self):
        driver = webdriver.Chrome(executable_path="C:/Users/kruthi.p/PycharmProjects/main/drivers/chromedriver.exe")
        driver.maximize_window()                # Method that maximize the window
        print("started")
        driver.get(Utils.URL)                   # get the EOT_C Web URL from the Utils page
        login_obj = LoginPage(driver)           # Object creation for loginpage class
        login_obj.Login("s@s.com","Sisa@123")   # Function call to login method ;1st parameter = emailid ; 2nd parameter = password;
        keyword_obj = Anomaly_management(driver)
        keyword_obj.anomaly_keyword_detection()
        #keyword_obj.AKM_add_keyword_button()
        driver.find_element_by_xpath("//*[@id='openDialogID']").click()
        time.sleep(3)
        keyword_obj.AKM_new_keyword_logstash_field("message")
        keyword_obj.AKM_new_keyword_match_condition("Match")
        keyword_obj.AKM_new_keyword_keyword_duration(2)
        keyword_obj.AKM_Keyword_add_keyword("dskfks")

        time.sleep(3)
        keyword_obj.AKM_new_keyword_cancel()
        expected_title = ">   Anomaly Keywords"
        element = driver.find_element_by_xpath("//*[@id='content']/h2/span").text
        print(element)
        self.assertEqual(expected_title, element, "title is not Anomaly Keywords")
        driver.close()
        driver.quit()

