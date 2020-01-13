class Manage_Alarm_Delete():
    def __init__(self, driver):
        self.driver = driver
        self.Manage_Alarm_Delete_Alarm_xpath = "/html/body/div[1]/div/div/section/div/article/div/div/div[1]/a[1]"
        self.Manage_Alarm_Manage_Alarm_Search_xpath = "/html/body/div[1]/div/div/section/div/article/div/div/div[2]/div/div[1]/div[1]/div/label/input"
        self.Manage_Alarm_Checkbox_All_xpath = "/html/body/div[1]/div/div/section/div/article/div/div/div[2]/div/table/thead/tr/th[1]/input"
        self.Manage_Alarm_Alarm_Delete_Confirmation_yes_id = "/html/body/div[9]/div/div/div/button[2]"
        self.Manage_Alarm_Alarm_Delete_Confirmation_no_id = "bot1-Msg1"


    def manage_alarm_click_delete_alarm(self):
        self.driver.find_element_by_xpath(self.Manage_Alarm_Delete_Alarm_xpath).click()

    def manage_alarm_confirmation(self,confirmation_id):
        if confirmation_id ==1:
            self.driver.find_element_by_xpath(self.Manage_Alarm_Alarm_Delete_Confirmation_yes_id).click()
        else:
            self.driver.find_element_by_id(self.Manage_Alarm_Alarm_Delete_Confirmation_no_id).click()

    def manage_alarm_enter_alarm_search(self, searchdata):
        self.driver.find_element_by_xpath(self.Manage_Alarm_Manage_Alarm_Search_xpath).send_keys(searchdata)

    def manage_alarm_click_all_checkbox(self):
        self.driver.find_element_by_xpath(self.Manage_Alarm_Checkbox_All_xpath).click()



    def Manage_alarm_delete(self,confirmation_id):
        self.manage_alarm_click_all_checkbox()
        self.manage_alarm_click_delete_alarm()
        self.manage_alarm_confirmation(confirmation_id)