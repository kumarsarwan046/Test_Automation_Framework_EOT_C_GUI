import time
from selenium.webdriver.common.action_chains import ActionChains

class AccessControlManagement():
    def __init__(self,driver):
        self.driver = driver
        self.ACS_click_create_user_xpath = "//*[@id='wid-id-0']/div/div[1]/button[1]"    # xpath of create user button
        self.ACS_click_view_audit_los_xpath = "//*[@id='wid-id-0']/div/div[1]/button[2]"        # xpath of view audit log button
        self.ACS_click_delete_button_xpath = "//*[@id='deletemultiple']"        # xpath of delete user button
        self.ACS_click_update_role_xpath = "//*[@id='dialog_updaterole']"        # xpath of update user role button
        self.ACS_click_main_checkbox = "//*[@id='checkBoxAll']"              # xpath of main checkbox
        self.ACS_click_delete_key_xpath = "//*[@id='dt_basic']/tbody/tr[1]/td[12]/a[2]" #xpath of delete key
