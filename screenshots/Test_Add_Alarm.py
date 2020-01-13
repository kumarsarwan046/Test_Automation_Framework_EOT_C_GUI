from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from utils import Utils
from pages.loginpage import LoginPage
from pages.Manager_Admin_ManageAlarm import Manage_Alarm
from pages.Manage_Alarm_Add import AlarmAdd
import pytest
@pytest.mark.usefixtures("test_setup")
class Test_Login():
    def test_login(self):
        driver = self.driver
        driver.get(Utils.URL)
        login = LoginPage(driver)
        login.Login("sisamanager@gmail.com","Sisa@123")
        admin = Manage_Alarm(driver)
        admin.click_admin()
        admin.click_manage_alarm()
        add_alarm = AlarmAdd(driver)
        add_alarm.add_alarm("test",1,1,1)

        time.sleep(3)

