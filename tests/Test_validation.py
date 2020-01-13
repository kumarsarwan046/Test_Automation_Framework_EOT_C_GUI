import unittest
import time
from selenium import webdriver

from utils import Utils
from pages.loginpage import LoginPage
from pages.Manage_User import Manage_User
from pages.User_Add import Add_user

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
        manage_user_obj.manage_user_user_add()  # Function call to manage_user_user_add method which performs : navigating to add user window from main page
        user_obj = Add_user(driver)             # Object creation for add_user class
        user = user_obj.add_user_enter_user_name("kruthi")
        user_obj.add_user_enter_email_id("kr@kr.com")
        user_obj.add_user_enter_phone_number(2342424)
        user_obj.add_user_enter_password("Sisa@123")
        user_obj.add_user_enter_confirm_password("Sisa@123")
        user_obj.add_user_select_user_role(4)
        user_obj.add_user_select_company()
        user_obj.add_user_click_save()

        driver.close()
        driver.quit()






