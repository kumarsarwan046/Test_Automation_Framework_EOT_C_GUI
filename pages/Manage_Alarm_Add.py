import time


class AlarmAdd():
    def __init__(self,driver):
        self.driver = driver
        self.Add_Alarm_click_xpath = "//*[@id='wid-id-0']/div/div[1]/button"        # Click on Add Alarm
        self.Enter_Alarm_name_id = "alarmname"                                      # Enter the Alarm Name
        self.Click_Status_xpath = "//*[@id='Status']"                               # Enter Alarm status
        self.click_enable_xpath = "//*[@id='Status']/option[2]"                     # xpath for enable
        self.click_disable_xapth = "//*[@id='Status']/option[3]"                    # xpath for disable
        self.click_severity_xpath = "//*[@id='severity']"                           # xpath for selecting the severity
        self.click_medium_xpath = "//*[@id='severity']/option[3]"                   # xpath for medium severity
        self.click_high_xpath = "//*[@id='severity']/option[2]"                     # xpath for high severity
        self.click_low_xpath = "//*[@id='severity']/option[4]"                      # xpath for low severity
        self.click_select_source_name_xpath ="/html/body/div[1]/div/div/section/div/article[2]/div/div/div[1]/div[2]/div/a/span[1]"  #xpath for selecting the source name
        self.click_remove_checkbox_id = "checkBoxAll1"                              # xpath for selecting the main checkbox
        self.click_select_plugin_xpath = "/html/body/div[9]/ul/li[2]/div"           # xpath for selecting the plugin id
        self.click_plugin_1 = "/html/body/div[9]/ul/li[2]/div"
        self.click_plugin_2 = "/html/body/div[9]/ul/li[3]/div"
        self.click_add_checkbox_id ="checkBoxAll"                                   # xpath for selecting the main checkbox of add events window
        self.click_Add_id = "btnAdd"                                                # xpath for Add Button in add events window
        self.click_Remove_id = "btnRemove"                                          # xpath for remove button in remove event window
        self.click_Alarm_save_id = "btnsave"                                        # xpath for saving the alarm
        self.click_plugin_remove_confirmation_yes = "//*[@id='bot2-Msg1']"          # xpath for delete confirmation alert_yes
        self.click_plugin_remove_confirmation_no = "//*[@id='bot1-Msg1']"           # xpath for delete confirmation alert_no


    # Function definition for add alarm
    def add_alarm_click(self):
        self.driver.find_element_by_xpath(self.Add_Alarm_click_xpath).click()

    # Function definition for entering the alarm name
    def add_alarm_enter_alarm_name(self, Alarm_Name):
        self.driver.find_element_by_xpath(self.Enter_Alarm_name_id).send_keys(Alarm_Name)

    # Function definition for saving the alarm
    def add_alarm_click_alarm_save(self):
        self.driver.find_element_by_id(self.click_Alarm_save_id).click()

    # Function definition for selecting the alarm status
    def add_alarm_click_alarm_status(self,status):
        self.driver.find_element_by_xpath(self.Click_Status_xpath).click()
        if status ==1 :
            self.driver.find_element_by_xpath(self.click_enable_xpath).click()
        elif status == 2 :
            self.driver.find_element_by_xpath(self.click_disable_xapth).click()

    # Function definition for selecting the severity
    def add_alarm_click_alarm_severity(self,severity):
        self.driver.find_element_by_xpath(self.click_severity_xpath).click()
        if severity ==1 :
            self.driver.find_element_by_xpath(self.click_high_xpath).click()
        elif severity == 2 :
            self.driver.find_element_by_xpath(self.click_medium_xpath).click()
        elif severity ==3:
            self.driver.find_element_by_xpath(self.click_low_xpath).click()

    # Function definition for selecting the plugin Id and adding the events
    def add_alarm_select_alarm_plugin_ID_add(self,plugin):
        self.driver.find_element_by_xpath(self.click_select_source_name_xpath).click()
        if plugin ==1 :
            self.driver.find_element_by_xpath(self.click_plugin_1).click()
        elif plugin == 2 :
            self.driver.find_element_by_xpath(self.click_plugin_2).click()
        self.driver.find_element_by_id(self.click_add_checkbox_id).click()
        self.driver.find_element_by_id(self.click_Add_id).click()

    # Function definition for selecting the plugin Id and removing the events
    def add_alarm_select_alarm_plugin_ID_remove(self,confirmation):
        self.driver.find_element_by_id(self.click_remove_checkbox_id).click()
        self.driver.find_element_by_id(self.click_Remove_id).click()
        if confirmation==1 :
            self.driver.find_element_by_xpath(self.click_plugin_remove_confirmation_yes).click()
        elif confirmation== 2 :
            self.driver.find_element_by_xpath(self.click_plugin_remove_confirmation_no).click()

    # Function definition for adding the alarm, that calls multiple function
    def add_alarm(self,alarm_name,status,severity,plugin):
        self.add_alarm_click()
        self.add_alarm_enter_alarm_name(alarm_name)
        self.add_alarm_click_alarm_status(status)
        self.add_alarm_click_alarm_severity(severity)
        self.add_alarm_select_alarm_plugin_ID_add(plugin)
        self.add_alarm_click_alarm_save()
        time.sleep(3)

    # To delete the plugin id selected while adding the alarm
    def remove_alarm_plugin_id(self,alarm_name,status,severity,plugin,confirmation):
        self.add_alarm_click()
        self.add_alarm_enter_alarm_name(alarm_name)
        self.add_alarm_click_alarm_status(status)
        self.add_alarm_click_alarm_severity(severity)
        self.add_alarm_select_alarm_plugin_ID_add(plugin)
        self.add_alarm_select_alarm_plugin_ID_remove(confirmation)
        time.sleep(3)
