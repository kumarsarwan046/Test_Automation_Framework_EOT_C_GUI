import unittest
from selenium import webdriver
import time
from utils import Utils
from pages.loginpage import LoginPage
from pages.manage_elastic_search_columns import elastic_search
class Test(unittest.TestCase):
    def test(self):
        driver = webdriver.Chrome(executable_path="C:/Users/kruthi.p/PycharmProjects/main/drivers/chromedriver.exe")
        driver.maximize_window()                # Method that maximize the window
        print("started")
        driver.get(Utils.URL)                   # get the EOT_C Web URL from the Utils page
        login_obj = LoginPage(driver)           # Object creation for loginpage class
        login_obj.Login("s@s.com","Sisa@123")   # Function call to login method ;1st parameter = emailid ; 2nd parameter = password;
        es_obj= elastic_search(driver)
        es_obj.add_es_column("records","records","eeee","logstash")
        time.sleep(1)
        es_obj.es_search("records")
        time.sleep(1)
        es_obj.es_checkbox()
        time.sleep(1)
        es_obj.es_delete()
        time.sleep(1)
        es_obj.es_delete_confirmation_yes()
        es = []

        length = len(driver.find_elements_by_xpath("//*[@id='dt_basic']/tbody/tr")) #Checking the number of records exist in user list table
        print(length)

        # Validation: To check whether added user is present in list or not ; If present " User Added Successfully will be printed, If not Exception will be raised

        for i in range(1,length+1):
            rows = driver.find_element_by_xpath("//*[@id='dt_basic']/tbody/tr[" + str(i) + "]/td[4]").text
            es.append(rows)
            print(rows)
        var = "records"
        self.assertNotIn(var,es)   #compares the value present in var with the user list






