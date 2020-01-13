from selenium import webdriver
import time
from pages.loginpage import LoginPage
from pages.Manager_Admin_ManageAlarm import Manage_Alarm
from pages.Manage_Alarm_Add import AlarmAdd
import pytest
@pytest.mark.usefixtures("test_setup")
class Test_login():
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
        add_alarm = AlarmAdd(driver)

        add_alarm.click_add_alarm()
        add_alarm.enter_alarm_name("Kruthi")
        #add_alarm.click_alarm_status()
        add_alarm.click_alarm_enable()
        #add_alarm.click_alarm_severity()
        add_alarm.click_alarm_high()
        add_alarm.click_alarm_source_name()
        add_alarm.click_alarm_select_plugin_id()
        driver.find_element_by_id("checkBoxAll").click()
        add_alarm.click_alarm_source_add()
        add_alarm.click_alarm_save()
        admin.click_all_checkbox()
        admin.click_update_alarm_severity()
        admin.click_select_severity_low()
        admin.click_alarm_severity_update_save()
        time.sleep(3)
