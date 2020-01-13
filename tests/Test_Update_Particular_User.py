import unittest
import allure
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
        users = []

        # Function call to add_user method(parameters : fullname,email id, phone number,password,confirm password,role id)

        user_obj.add_user("kruthi","kr@kr.com",8552426,"Sisa@123","Sisa@123",5)
        length = len(driver.find_elements_by_xpath("//*[@id='dt_basic']/tbody/tr")) #Checking the number of records exist in user list table
        print(length)
        value = 'kr@kr.com'
        print("before modification")
        for i in range(1,length+1):
            rows = driver.find_element_by_xpath("//*[@id='dt_basic']/tbody/tr["+str(i)+"]/td[3]").text
            users.append(rows)
            print(rows)
        if value in users:
            manage_user_obj.manage_user_search("kr@kr.com")
            manage_user_obj.manage_user_edit_key()
            user_obj.add_user_enter_email_id("k@k.com")
            user_obj.add_user_edit_update()
            time.sleep(3)

        length = len(driver.find_elements_by_xpath("//*[@id='dt_basic']/tbody/tr")) #Checking the number of records exist in user list table
        print(length)

# Validation: To check whether added user is present in list or not ; If present " User Added Successfully will be printed, If not Exception will be raised
        modified_value = "k@k.com"
        print("after modification")
        for i in range(1,length+1):
            rows = driver.find_element_by_xpath("//*[@id='dt_basic']/tbody/tr["+str(i)+"]/td[3]").text
            users.append(rows)
            print(rows)
        self.assertIn(modified_value,users)   #compares the value present in value with the user list



