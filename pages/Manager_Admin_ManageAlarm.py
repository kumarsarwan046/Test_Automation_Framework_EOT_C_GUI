from selenium.webdriver.common.action_chains import ActionChains
class Manage_Alarm():
    def __init__(self, driver):
        self.driver = driver
        self.Admin_click_xpath = "/html/body/aside/nav/ul/li[8]/a/span"
        self.ManageAlarm_click_xpath = "/html/body/aside/nav/ul/li[8]/ul/li[2]/a"
        self.Delete_Alarm_xpath = "/html/body/div[1]/div/div/section/div/article/div/div/div[1]/a[1]"
        self.Update_Alarm_Severity = "/html/body/div[1]/div/div/section/div/article/div/div/div[1]/a[2]"
        self.Manage_Alarm_Search_xpath = "/html/body/div[1]/div/div/section/div/article/div/div/div[2]/div/div[1]/div[1]/div/label/input"
        self.Manage_Alarm_Checkbox_All_xpath = "/html/body/div[1]/div/div/section/div/article/div/div/div[2]/div/table/thead/tr/th[1]/input"
        self.Alarm_Delete_Confirmation_yes_id = "/html/body/div[9]/div/div/div/button[2]"
        self.Alarm_Delete_Confirmation_no_id = "bot1-Msg1"
        self.Alarm_Update_Select_severity_id = "updateseverity"
        self.Alarm_update_high_xpath = "/html/body/div[7]/div[2]/select/option[2]"
        self.Alarm_update_low_xpath = "/html/body/div[7]/div[2]/select/option[4]"
        self.Alarm_update_medium_xpath = "/html/body/div[7]/div[2]/select/option[3]"
        self.Alarm_click_update_xpath = "/html/body/div[7]/div[3]/div/button[1]"
        self.Alarm_click_update_cancel_xpath = "/html/body/div[7]/div[3]/div/button[2]"

    def click_admin(self):
        elements_to_hover_over = self.driver.find_element_by_xpath(self.Admin_click_xpath)  # Keeping Cursor on User Module
        hover = ActionChains(self.driver).move_to_element(elements_to_hover_over)
        hover.perform()

    def click_manage_alarm(self):
        self.driver.find_element_by_xpath(self.ManageAlarm_click_xpath).click()

    def click_delete_alarm(self):
        self.driver.find_element_by_xpath(self.Delete_Alarm_xpath).click()

    def click_alarm_confirmation_yes(self):
        self.driver.find_element_by_xpath(self.Alarm_Delete_Confirmation_yes_id).click()

    def click_alarm_confirmation_no(self):
        self.driver.find_element_by_id(self.Alarm_Delete_Confirmation_no_id).click()

    def click_update_alarm_severity(self):
        self.driver.find_element_by_xpath(self.Update_Alarm_Severity).click()

    def enter_alarm_search(self, searchdata):
        self.driver.find_element_by_xpath(self.Manage_Alarm_Search_xpath).send_keys(searchdata)

    def click_all_checkbox(self):
        self.driver.find_element_by_xpath(self.Manage_Alarm_Checkbox_All_xpath).click()

    def click_select_severity(self):
        self.driver.find_element_by_xpath(self.Alarm_Update_Select_severity_id).click()

    def click_select_severity_high(self):
        self.driver.find_element_by_xpath(self.Alarm_update_high_xpath).click()

    def click_select_severity_low(self):
        self.driver.find_element_by_xpath(self.Alarm_update_low_xpath).click()

    def click_select_severity_medium(self):
        self.driver.find_element_by_xpath(self.Alarm_update_medium_xpath).click()

    def click_alarm_severity_update_save(self):
        self.driver.find_element_by_xpath(self.Alarm_click_update_xpath).click()

    def click_alarm_severity_update_cancel(self):
        self.driver.find_element_by_xpath(self.Alarm_click_update_cancel_xpath).click()

