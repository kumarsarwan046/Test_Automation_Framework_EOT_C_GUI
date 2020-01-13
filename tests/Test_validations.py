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
        print(driver.title)
        manage_user_obj.manage_user_user_add()  # Function call to manage_user_user_add method which performs : navigating to add user window from main page
        time.sleep(3)
        #user_obj = Add_user(driver)             # Object creation for add_user class
        #users = []
        driver.find_element_by_id("FullName").send_keys("abcddk")
        time.sleep(2)
        driver.find_element_by_id("Email").send_keys("kdhjkd@jkldjk.com")
        driver.find_element_by_id("PhoneNumber").send_keys(231421421)
        driver.find_element_by_id("Password").send_keys("Sisa@123")
        driver.find_element_by_id("ConfirmPassword").send_keys("Sisa@123")
        driver.find_element_by_xpath("//*[@id='user_role']").click()
        driver.find_element_by_xpath("//*[@id='user_role']/option[2]").click()
        driver.find_element_by_id("s2id_company_name").click()
        driver.find_element_by_id("s2id_autogen1_search").send_keys("SISA KRUTHI (C-0010080)")

        driver.find_element_by_xpath("//*[@id='company_name']/option[11]").click()
        driver.find_element_by_id("btnSave").click()

        time.sleep(3)
