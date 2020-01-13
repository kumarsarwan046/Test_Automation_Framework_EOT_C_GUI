import unittest
from selenium import webdriver
import time
from utils import Utils
from pages.loginpage import LoginPage
from pages.Manage_User import Manage_User

class Test(unittest.TestCase):
    def test(self):
        driver = webdriver.Chrome(executable_path="C:/Users/kruthi.p/PycharmProjects/Test_Automation_Framework/drivers/chromedriver.exe")
        driver.maximize_window()                        # Method that maximize the window
        print("started")
        driver.get(Utils.URL)                           # get the EOT_C Web URL from the Utils page
        login_obj = LoginPage(driver)                   # Object creation for loginpage class
        login_obj.Login("s@s.com","Sisa@123")           # Function call to login method ;1st parameter = emailid ; 2nd parameter = password;
        manage_user_obj = Manage_User(driver)           # Object creation for manage_user class
        manage_user_obj.manage_user_click()             # Function call to manage_user_user_add method which performs : navigating to add user window from main page
        manage_user_obj.manage_user_delete_all_user()


        # Function call to delete_all_user method which performs : select all the user and clicks on delete
        time.sleep(3)
        value = 1
        length = len(driver.find_elements_by_xpath("//*[@id='dt_basic']/tbody/tr"))
        print(length)
        self.assertEqual(length,value)



