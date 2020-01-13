import unittest
from selenium import webdriver
import time
from utils import Utils
from pages.loginpage import LoginPage
from pages.Anomaly_keyword_Management import Anomaly_management
class Test(unittest.TestCase):
    def test(self):
        global rows_exist
        driver = webdriver.Chrome(executable_path="C:/Users/kruthi.p/PycharmProjects/Test_Automation_Framework/drivers/chromedriver.exe")
        driver.maximize_window()                # Method that maximize the window
        print("started")
        driver.get(Utils.URL)                   # get the EOT_C Web URL from the Utils page
        login_obj = LoginPage(driver)           # Object creation for loginpage class
        login_obj.Login("s@s.com","Sisa@123")   # Function call to login method ;1st parameter = emailid ; 2nd parameter = password;
        keyword_obj = Anomaly_management(driver)
        keyword_obj.anomaly_keyword_detection()
        keyword_before = []
        keyword_after = []
        length = len(driver.find_elements_by_xpath("//*[@id='dt_basic']/tbody/tr"))  # Checking the number of records exist in user list table
        print(length)
        value = 'rewfwef'
        for i in range(1, length + 1):
            rows = driver.find_element_by_xpath("//*[@id='dt_basic']/tbody/tr[" + str(i) + "]/td[6]").text
            keyword_before.append(rows)
            #print(keyword_before)

        if value in keyword_before:
            # driver.find_element_by_xpath("//*[@id='dt_basic_filter']/label/input").click()
            # driver.find_element_by_xpath("//*[@id='dt_basic_filter']/label/input").send_keys("refeerf")
            time.sleep(3)
            keyword_obj.AKM_search("refeerf")
            keyword_obj.AKM_delete_particular()

  # Validation: To check whether added user is present in list or not ; If present " User Added Successfully will be printed, If not Exception will be raised
        length_post = len(driver.find_elements_by_xpath("//*[@id='dt_basic']/tbody/tr"))
        print(length_post)
        for i in range(1, length_post):
            rows_exist = driver.find_element_by_xpath("//*[@id='dt_basic']/tbody/tr[" + str(i) + "]/td[6]").text
            keyword_after.append(rows_exist)
            print(keyword_after)
        self.assertIn(value, keyword_after)  # compares the value present in value with the user list

        driver.close()
        driver.quit()




