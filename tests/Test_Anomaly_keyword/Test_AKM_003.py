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
        keyword_obj.AKM_add_anomaly_keyword("Message","Match",2,"kruthi1")
        keyword_list=[]
        length = len(driver.find_elements_by_xpath("//*[@id='dt_basic']/tbody/tr")) #Checking the number of records exist in user list table
        print(length)

        # Validation: To check whether added user is present in list or not ; If present " User Added Successfully will be printed, If not Exception will be raised

        for i in range(1,length+1):
            rows = driver.find_element_by_xpath("//*[@id='dt_basic']/tbody/tr["+ str(i) +"]/td[6]").text
            keyword_list.append(rows)
            print(rows)
        var = "kruthi1"
        self.assertIn(var,keyword_list)
        driver.close()
        driver.quit()




