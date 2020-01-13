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
        es_obj.manage_elastic_search()
        expected_title ="> Manage Elasticsearch Columns"
        element = driver.find_element_by_xpath("//*[@id='content']/div/div/h1/span").text
        print(element)
        self.assertEqual(expected_title,element,"title is not manage elasticsearch column")
        driver.close()
        driver.quit()




