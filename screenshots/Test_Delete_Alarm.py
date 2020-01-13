from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from pages.loginpage import LoginPage
from pages.Manager_Admin_ManageAlarm import Manage_Alarm
from pages.Manage_Alarm_Add import AlarmAdd
from pages.Manage_Alarm_Delete import Manage_Alarm_Delete
import pytest
@pytest.mark.usefixtures("test_setup")
class Test_Login():
    def test_login(self):
        driver = self.driver
        driver.get("https://10.100.13.30/")
        login = LoginPage(driver)
        login.enter_email_id("sisamanager@gmail.com")
        login.enter_password("Sisa@123")
        login.click_login()
        admin = Manage_Alarm(driver)
        admin.click_admin()
        admin.click_manage_alarm()
        delete = Manage_Alarm_Delete(driver)

        delete.enter_alarm_search("kruthi")
        delete.click_all_checkbox()
        delete.click_delete_alarm()
        delete.click_alarm_confirmation_yes()
       # admin.click_alarm_confirmation_no()
        time.sleep(3)
