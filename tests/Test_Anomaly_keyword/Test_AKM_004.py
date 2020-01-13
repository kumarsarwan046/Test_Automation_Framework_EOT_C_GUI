import unittest
from selenium import webdriver
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
        keyword_obj.AKM_add_keyword_button()
        time.sleep(3)
        keyword_obj.AKM_add_anomaly_keyword("Message","Match","adf","kruthi1")
        expected_title ="Add New Keyword"
        time.sleep(3)
        element = driver.find_element_by_xpath("//*[@id='ui-id-1']").text
        print(element)
        self.assertEqual(expected_title,element,"title is not Add New Keyword")

        driver.close()
        driver.quit()




