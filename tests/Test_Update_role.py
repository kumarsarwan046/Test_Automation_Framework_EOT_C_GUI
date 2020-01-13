import unittest
import allure
import time
from selenium import webdriver

from utils import Utils
from pages.loginpage import LoginPage
from pages.Manage_User import Manage_User

# class Fail(Exception):
#         #"""Base class for exceptions in this module."""
#         #def call(self):
#             #print('user not added')
#         #pass"""

class Test(unittest.TestCase):
    def test(self):
        driver = webdriver.Chrome(executable_path="C:/Users/kruthi.p/PycharmProjects/Test_Automation_Framework/drivers/chromedriver.exe")
        driver.maximize_window()                # Method that maximize the window
        print("started")
        driver.get(Utils.URL)                   # get the EOT_C Web URL from the Utils page
        login_obj = LoginPage(driver)           # Object creation for loginpage class
        login_obj.Login("s@s.com","Sisa@123")   # Function call to login method ;1st parameter = emailid ; 2nd parameter = password;
        manage_user_obj = Manage_User(driver)   # Object creation for manage_user class
        manage_user_obj.manage_user_user_add()
        driver.find_element_by_xpath("//*[@id='checkBoxAll']").click()
        time.sleep(3)
        manage_user_obj.manage_user_Update_button(4)
        time.sleep(3)

