from selenium.webdriver.common.action_chains import ActionChains
import time
class elastic_search:
    def __init__(self,driver):
        self.driver=driver
        self.ES_Page_title_xpath = "//*[@id='content']/div/div/h1/span"
        self.ES_importcolumns_from_ES_xpath = "//*[@id='btn_import_column']"
        self.ES_add_columns_button_xpath = "//*[@id='btnadd']"
        self.ES_delete_button_xpath = "//*[@id='deletemultiple']"
        self.ES_delete_confirmation_yes_xpath = "//*[@id='bot2-Msg1']"
        self.ES_delete_confirmation_no_xpath = "//*[@id='bot1-Msg1']"
        self.ES_search_xpath = "//*[@id='dt_basic_filter']/label/input"
        self.ES_main_checkbox_xpath = "//*[@id='checkBoxAll']"
       # self.ES_edit_key_xpath = "//*[@id="dt_basic"]/tbody/tr[1]/td[9]/a[1]"
        self.ES_add_columnname_xpath = "//*[@id='es_column_name']"
        self.ES_add_displayname_xpath = "//*[@id='display_column_name']"
        self.ES_add_description_xpath = "//*[@id='description']"
        self.ES_display_column_name_xpath = "//*[@id='s2id_index_id']"
        self.ES_column_name_logstash_xpath = "//*[@id='select2-result-label-4']"
        self.ES_Column_name_mastercorrelationhistory_xpath = "//*[@id='select2-result-label-5']"
        self.ES_Column_name_netflow_xpath = "//*[@id='select2-result-label-6']"
        self.ES_Column_name_device_monitor_xpath = "//*[@id='select2-result-label-7']"
        self.ES_Column_name_netflow_threathunting_xpath = "//*[@id='select2-result-label-8']"
        self.ES_Column_name_email_template_common_xpath = "//*[@id='select2-result-label-9']"
        self.ES_display_option_xpath = "//*[@id='enable']"
        self.ES_enable_search_option_xpath = "//*[@id='is_searchable']"
        self.ES_add_column_save_xpath = "//*[@id='btnSave']"
        self.ES_add_column_Cancel_xpath = "//*[@id='wid-id-4']/div/div[7]/div/button"


    def manage_elastic_search(self):
        self.elements_to_hover_over = self.driver.find_element_by_xpath("//*[@id='left-panel']/nav/ul/li[6]/a/span")  # Keeping Cursor on Admin Module
        self.hover = ActionChains(self.driver).move_to_element(self.elements_to_hover_over)
        self.hover.perform()
        self.driver.find_element_by_xpath("//*[@id='left-panel']/nav/ul/li[6]/ul/li[2]/a").click()

    def add_es_button(self):
        self.driver.find_element_by_xpath(self.ES_add_columns_button_xpath).click()

    def add_es_column_name(self,name):
        #self.driver.find_element_by_xpath(self.ES_add_columnname_xpath).clear()
        self.driver.find_element_by_xpath(self.ES_add_columnname_xpath).send_keys(name)
        time.sleep(3)

    def add_es_display_name(self,display_name):
        self.driver.find_element_by_xpath(self.ES_add_displayname_xpath).clear()
        self.driver.find_element_by_xpath(self.ES_add_displayname_xpath).send_keys(display_name)

    def add_es_description(self,description):
        self.driver.find_element_by_xpath(self.ES_add_description_xpath).clear()
        self.driver.find_element_by_xpath(self.ES_add_description_xpath).send_keys(description)

    def add_display_column(self,column_option):
        self.driver.find_element_by_xpath(self.ES_display_column_name_xpath).click()
        if column_option == "logstash":
            self.driver.find_element_by_xpath(self.ES_column_name_logstash_xpath).click()
        elif column_option == "correlation":
            self.driver.find_element_by_xpath(self.ES_Column_name_mastercorrelationhistory_xpath).click()
        elif column_option == "netflow":
            self.driver.find_element_by_xpath(self.ES_Column_name_netflow_xpath).click()
        elif column_option == "device_monitor":
            self.driver.find_element_by_xpath(self.ES_Column_name_device_monitor_xpath).click()
        elif column_option == "netflow_threathunting":
            self.driver.find_element_by_xpath(self.ES_Column_name_netflow_threathunting_xpath).click()
        elif column_option == "email_template":
            self.driver.find_element_by_xpath(self.ES_Column_name_email_template_common_xpath).click()

    def display_option(self):
        self.driver.find_element_by_xpath(self.ES_display_option_xpath).click()

    def enable_search_option(self):
        self.driver.find_element_by_xpath(self.ES_search_xpath).click()

    def es_save(self):
        self.driver.find_element_by_xpath(self.ES_add_column_save_xpath).click()

    def es_cancel(self):
        self.driver.find_element_by_xpath(self.ES_add_column_Cancel_xpath).click()

    def es_search(self,search):
        self.driver.find_element_by_xpath(self.ES_search_xpath).clear()
        self.driver.find_element_by_xpath(self.ES_search_xpath).send_keys(search)

    def es_checkbox(self):
        self.driver.find_element_by_xpath(self.ES_main_checkbox_xpath).click()

    def es_delete(self):
        self.driver.find_element_by_xpath(self.ES_delete_button_xpath).click()

    def es_delete_confirmation_yes(self):
        self.driver.find_element_by_xpath(self.ES_delete_confirmation_yes_xpath).click()

    def es_delete_confirmation_no(self):
        self.driver.find_element_by_xpath(self.ES_delete_confirmation_no_xpath).click()

    def add_es_column(self,column_name,displayname,desc,display_columnname):
        self.manage_elastic_search()
        self.add_es_button()
        self.add_es_column_name(column_name)
        self.add_es_display_name(displayname)
        self.add_es_description(desc)
        self.add_display_column(display_columnname)
        self.es_save()



