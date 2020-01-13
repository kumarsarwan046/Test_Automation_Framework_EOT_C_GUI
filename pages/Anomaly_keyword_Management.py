from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
class Anomaly_management():
    def __init__(self,driver):
        self.driver = driver
        self.AKM_add_keyword_button_xpath = "//*[@id='openDialogID']"
        self.AKM_delete_button_xpath = "//*[@id='deletemultiple']"
        self.AKM_main_checkbox_xpath = "//*[@id='checkBoxAll']"
        self.AKM_search_box_xpath = "//*[@id='dt_basic_filter']/label/input"
        self.AKM_edit_key_class = "editbtn"
        self.AKM_edit_logstash_field_xpath = "//*[@id='ddl_es_field_name_edit']"
        self.AKM_edit_match_condition_xpath = "//*[@id='ddl_condition_edit']"
        self.AKM_edit_duration_xpath = "//*[@id='DurationIDForEdit']"
        self.AKM_edit_keyword_textbox_xpath = "//*[@id='txtValuediv']/div/input"
        self.AKM_edit_keyword_save_xpath = "/html/body/div[8]/div[3]/div/button[1]"
        self.AKM_edit_keyword_cancel_xpath = "/html/body/div[8]/div[3]/div/button[2]"
        self.AKM_delete_key_class = "deletebtn"
        self.AKM_delete_confirmation_yes_xpath = "//*[@id='bot2-Msg1']"
        self.AKM_delete_confirmation_no_xpath = "//*[@id='bot1-Msg1']"
        self.AKM_New_keyword_message_xpath = "//*[@id='ddl_column']"
        self.AKM_New_keyword_condition_match_xpath = "//*[@id='ddl_condition']"
        self.AKM_New_keyword_duration_xpath ="//*[@id='DurationID']"
        self.AKM_New_keyword_add_textbox_xpath = "//*[@id='txtValuediv']/div/input"
        self.AKM_New_keyword_add_button_xpath = "/html/body/div[7]/div[3]/div/button[1]"
        self.AKM_New_keyword_close_button_xpath = "/html/body/div[7]/div[3]/div/button[2]"


    def anomaly_keyword_detection(self):
        self.elements_to_hover_over = self.driver.find_element_by_xpath("//*[@id='left-panel']/nav/ul/li[6]/a/span")  # Keeping Cursor on Admin Module
        self.hover = ActionChains(self.driver).move_to_element(self.elements_to_hover_over)
        self.hover.perform()
        self.driver.find_element_by_xpath("//*[@id='left-panel']/nav/ul/li[6]/ul/li[4]/a").click()


    def AKM_add_keyword_button(self):
        self.driver.find_element_by_xpath(self.AKM_add_keyword_button_xpath).click()
        time.sleep(3)

    def AKM_new_keyword_logstash_field(self,logstash_field):
        self.driver.find_element_by_xpath(self.AKM_New_keyword_message_xpath).click()
        if logstash_field =="message":
            self.driver.find_element_by_xpath("//*[@id='ddl_column']/option[1]").click()
        elif logstash_field == "Host Name":
            self.driver.find_element_by_xpath("//*[@id='ddl_column']/option[2]").click()
        elif logstash_field == "Source IP":
            self.driver.find_element_by_xpath("//*[@id='ddl_column']/option[3]").click()
        elif logstash_field == "log_sub_type":
            self.driver.find_element_by_xpath("//*[@id='ddl_column']/option[4]").click()
        elif logstash_field == "log_type":
            self.driver.find_element_by_xpath("//*[@id='ddl_column']/option[5]").click()
        elif logstash_field == "logger_name":
            self.driver.find_element_by_xpath("//*[@id='ddl_column']/option[6]").click()
        elif logstash_field == "path":
            self.driver.find_element_by_xpath("//*[@id='ddl_column']/option[7]").click()
        elif logstash_field == "source":
            self.driver.find_element_by_xpath("//*[@id='ddl_column']/option[8]").click()
        elif logstash_field == "type":
            self.driver.find_element_by_xpath("//*[@id='ddl_column']/option[9]").click()
        elif logstash_field == "engine_id":
            self.driver.find_element_by_xpath("//*[@id='ddl_column']/option[10]").click()
        elif logstash_field == "engine_log_id":
            self.driver.find_element_by_xpath("//*[@id='ddl_column']/option[11]").click()
        elif logstash_field == "Records":
            self.driver.find_element_by_xpath("//*[@id='ddl_column']/option[12]").click()
        elif logstash_field == "username":
            self.driver.find_element_by_xpath("//*[@id='ddl_column']/option[2]").click()
        elif logstash_field == "Clientkey":
            self.driver.find_element_by_xpath("//*[@id='ddl_column']/option[3]").click()
        elif logstash_field == "@version":
            self.driver.find_element_by_xpath("//*[@id='ddl_column']/option[4]").click()
        elif logstash_field == "date":
            self.driver.find_element_by_xpath("//*[@id='ddl_column']/option[5]").click()
        elif logstash_field == "dst_ip":
            self.driver.find_element_by_xpath("//*[@id='ddl_column']/option[6]").click()
        elif logstash_field == "geoip":
            self.driver.find_element_by_xpath("//*[@id='ddl_column']/option[7]").click()
        elif logstash_field == "host":
            self.driver.find_element_by_xpath("//*[@id='ddl_column']/option[8]").click()
        elif logstash_field == "sport":
            self.driver.find_element_by_xpath("//*[@id='ddl_column']/option[9]").click()
        elif logstash_field == "alarm_name":
            self.driver.find_element_by_xpath("//*[@id='ddl_column']/option[10]").click()
        elif logstash_field == "Impact":
            self.driver.find_element_by_xpath("//*[@id='ddl_column']/option[11]").click()
        elif logstash_field == "solution":
            self.driver.find_element_by_xpath("//*[@id='ddl_column']/option[12]").click()


    def AKM_new_keyword_match_condition(self,condition):
        self.driver.find_element_by_xpath(self.AKM_New_keyword_condition_match_xpath).click()
        if condition == "Match":
            self.driver.find_element_by_xpath("//*[@id='ddl_condition']/option[1]").click()
        elif condition == "Fuzzy":
            self.driver.find_element_by_xpath("//*[@id='ddl_condition']/option[2]").click()

    def AKM_new_keyword_keyword_duration(self,duration):
        self.driver.find_element_by_xpath(self.AKM_New_keyword_duration_xpath).clear()
        self.driver.find_element_by_xpath(self.AKM_New_keyword_duration_xpath).send_keys(duration)

    def AKM_Keyword_add_keyword(self,keyword):
        keyword_elem = self.driver.find_element_by_xpath(self.AKM_New_keyword_add_textbox_xpath)
        keyword_elem.send_keys(keyword)
        keyword_elem.send_keys(Keys.ENTER)
        keyword_elem.send_keys(Keys.RETURN)


    def AKM_new_keyword_save(self):
        self.driver.find_element_by_xpath(self.AKM_New_keyword_add_button_xpath).click()

    def AKM_new_keyword_cancel(self):
        self.driver.find_element_by_xpath(self.AKM_New_keyword_close_button_xpath).click()

    def AKM_search(self,search_word):
        self.driver.find_element_by_xpath(self.AKM_search_box_xpath).click()
        self.driver.find_element_by_xpath(self.AKM_search_box_xpath).send_keys(search_word)

    def AKM_main_checkbox(self):
        self.driver.find_element_by_xpath(self.AKM_main_checkbox_xpath).click()

    def AMK_delete_button(self):
        self.driver.find_element_by_xpath(self.AKM_delete_button_xpath).click()

    def AKM_delete_confirmation_yes(self):
        self.driver.find_element_by_xpath(self.AKM_delete_confirmation_yes_xpath).click()

    def AKM_delete_confirmation_no(self):
        self.driver.find_element_by_xpath(self.AKM_delete_confirmation_no_xpath).click()

    def AKM_delete_key(self):
        self.driver.find_element_by_class_name(self.AKM_delete_key_class).click()

    def AKM_edit_key(self):
        self.driver.find_element_by_class_name(self.AKM_edit_key_class).click()

    def AKM_edit_logstash_field(self,logstash_field):
        self.driver.find_element_by_xpath(self.AKM_edit_logstash_field_xpath).click()

    def AKM_edit_match_condition(self,match_condition):
        self.driver.find_element_by_xpath(self.AKM_New_keyword_condition_match_xpath).click()
        if match_condition == "Match":
            self.driver.find_element_by_xpath("//*[@id='ddl_condition_edit']/option[1]").click()
        elif match_condition == "Fuzzy":
            self.driver.find_element_by_xpath("//*[@id='ddl_condition_edit']/option[2]").click()

    def AKM_edit_duration(self,duration):
        self.driver.find_element_by_xpath(self.AKM_edit_duration_xpath).clear()
        self.driver.find_element_by_xpath(self.AKM_edit_duration_xpath).send_keys(duration)

    def AKM_edit_keyword_textbox(self,keyword):
        self.driver.find_element_by_xpath(self.AKM_edit_keyword_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.AKM_edit_keyword_textbox_xpath).send_keys(keyword)

    def AKM_edit_save(self):
        self.driver.find_element_by_xpath(self.AKM_edit_keyword_save_xpath).click()
    def AKM_edit_cancel(self):
        self.driver.find_element_by_xpath(self.AKM_edit_keyword_cancel_xpath).click()

    def AKM_add_anomaly_keyword(self,logstash_field,condition,duration,keyword):

        self.AKM_new_keyword_logstash_field(logstash_field)
        time.sleep(3)
        self.AKM_new_keyword_match_condition(condition)
        time.sleep(3)
        self.AKM_new_keyword_keyword_duration(duration)
        time.sleep(3)
        self.AKM_Keyword_add_keyword(keyword)
        time.sleep(3)
        self.AKM_new_keyword_save()

    def AKM_edit_anomaly_keyword(self,logstash_field,condition,duration,keyword):
        self.AKM_edit_key()
        self.AKM_edit_logstash_field(logstash_field)
        self.AKM_edit_match_condition(condition)
        self.AKM_edit_duration(duration)
        self.AKM_edit_keyword_textbox(keyword)
        self.AKM_edit_cancel()

    def AKM_delete_particular(self):
        self.AKM_delete_key()
        self.AKM_delete_confirmation_yes()













