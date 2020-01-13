import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from utils import Utils
from pages.loginpage import LoginPage
from pages.Anomaly_keyword_Management import Anomaly_management
class Test(unittest.TestCase):
    def test(self):
        driver = webdriver.Chrome(executable_path="C:/Users/kruthi.p/PycharmProjects/Test_Automation_Framework/drivers/chromedriver.exe")
        driver.maximize_window()                # Method that maximize the window
        print("started")
        driver.get(Utils.URL)                   # get the EOT_C Web URL from the Utils page
        login_obj = LoginPage(driver)           # Object creation for loginpage class
        login_obj.Login("s@s.com","Sisa@123")   # Function call to login method ;1st parameter = emailid ; 2nd parameter = password;
        keyword_obj = Anomaly_management(driver)
        keyword_obj.anomaly_keyword_detection()
        time.sleep(3)
        keyword_obj.AKM_main_checkbox()
        time.sleep(3)
        keyword_obj.AMK_delete_button()
        keyword_obj.AKM_delete_confirmation_yes()
        value = 1
        length = len(driver.find_elements_by_xpath("//*[@id='dt_basic']/tbody/tr"))
        print(length)
        self.assertEqual(length,value,"1 or more Records exist in the table")

        time.sleep(3)
        driver.quit()

