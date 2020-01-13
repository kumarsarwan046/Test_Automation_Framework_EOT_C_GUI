import time
from selenium.webdriver.common.action_chains import ActionChains
class Manage_User():
    def __init__(self,driver):

        self.driver = driver
        self.Click_Adduser_xpath = "//*[@id='wid-id-0']/div/div[1]/div/div[1]/button"       # xpath of add user button
        self.Click_Delete_Button_id = "deletemultiple"                                      # id of delete button
        self.Click_Update_Button_id = "dialog_updaterole"                                   # id of update button
        self.Click_Select_Company_id = "select2-drop-mask"                                  # id of select company dropdown
        self.Select_Main_Checkbox_xpath = "//*[@id='checkBoxAll']"                          # xpath of main checkbox
        self.Previous_Page_xpath = "//*[@id='dt_basic_previous']/a"                         # xpath of previous page
        self.Next_Page_xpath = "//*[@id='dt_basic_next']/a"                                 # xpath of next page
        self.Pagination_xpath ="//*[@id='dt_basic_length']/label/select"                    # xpath of selecting records per page
        self.Pagination_10_xpath = "//*[@id='dt_basic_length']/label/select/option[1]"      # xpath of 10 records per page
        self.Pagination_25_xpath = "//*[@id='dt_basic_length]/label/select/option[2]"       # xpath of 25 records per page
        self.Pagination_50_xpath = "//*[@id='dt_basic_length']/label/select/option[3]"      # xpath of 50 records per page
        self.Pagination_100_xpath = "//*[@id='dt_basic_length']/label/select/option[4]"     # xpath of 100 records per page
        self.Search_xpath = "//*[@id='dt_basic_filter']/label/input"                        # xpath of search option
        self.Edit_Key_xpath = "//*[@id='dt_basic']/tbody/tr/td[7]/a[1]"                  # xpath of edit key
        self.Delete_Key_xpath = "/html/body/div[1]/div[1]/div/section/div/article/div/div/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[7]/a[2]" # xpath of delete key
        self.Delete_Confirmation_Yes_xpath = "/html/body/div[8]/div/div/div/button[2]"      # xpath of confirmation alert with option "yes"
        self.Delete_Confirmation_No_xpath = "//*[@id='bot1-Msg1']"                           # xpath of confirmation alert with option "no"
        self.Update_Button_Update_xpath = "/html/body/div[7]/div[3]/div/button[1]"           # xpath of update button present inside update role window"
        self.Update_Button_Cancel_xpath = "/html/body/div[9]/div[3]/div/button[2]"          # xpath of cancel button present inside update role window"

# Function definition for clicking on manage user under User Module
    def manage_user_click(self):
        self.elements_to_hover_over = self.driver.find_element_by_xpath("/html/body/aside/nav/ul/li[2]/a/span")  # Keeping Cursor on User Module
        self.hover = ActionChains(self.driver).move_to_element(self.elements_to_hover_over)
        self.hover.perform()
        self.driver.find_element_by_xpath("//*[@id='left-panel']/nav/ul/li[2]/ul/li/a").click()  # Click on Manage User

# Function definition for clicking on add user under manage user page of user Module
    def manage_user_add_user(self):
        self.driver.find_element_by_xpath(self.Click_Adduser_xpath).click()

# Function definition for clicking on delete user under manage user page of user Module
    def manage_user_delete_user(self):
        self.driver.find_element_by_id(self.Click_Delete_Button_id).click()

# Function definition for selecting the company under manage user page of user Module
    def manage_user_select_company(self):
        elements_to_hover_over = self.driver.find_element_by_xpath(self.Click_Select_Company_id)  # Keeping Cursor on User Module
        hover = ActionChains(self.driver).move_to_element(elements_to_hover_over)
        hover.perform()

# Function definition for selecting the number of records that should be dispayed on a page under manage user page of user Module

    def manage_user_record_per_page(self,records_per_page):
        self.driver.find_element_by_id(self.Pagination_xpath).click()
        if records_per_page==10 :
            self.driver.find_element_by_xpath(self.Pagination_10_xpath).click()
        elif records_per_page== 25 :
            self.driver.find_element_by_xpath(self.Pagination_25_xpath).click()
        elif records_per_page== 50 :
            self.driver.find_element_by_xpath(self.Pagination_50_xpath).click()
        elif records_per_page ==100:
            self.driver.find_element_by_xpath(self.Pagination_100_xpath).click()

# Function definition for search option under manage user page of user Module
    def manage_user_search(self,search_word):
        self.driver.find_element_by_xpath(self.Search_xpath).send_keys(search_word)
        time.sleep(3)

# Function definition for selecting the main check box present under manage user page of user Module
    def manage_user_main_checkbox(self):
        self.driver.find_element_by_xpath(self.Select_Main_Checkbox_xpath).click()
        time.sleep(3)

    def manage_user_previous_page(self):
        self.driver.find_element_by_xpath(self.Previous_Page_xpath).click()

    def manage_user_next_page(self):
        self.driver.find_element_by_xpath(self.Next_Page_xpath).click()

    def manage_user_edit_key(self):
        self.driver.find_element_by_xpath(self.Edit_Key_xpath).click()

    def manage_user_delete_key(self):
        self.driver.find_element_by_xpath(self.Delete_Key_xpath).click()

    def manage_user_delete_confirmation_yes(self):
        self.driver.find_element_by_xpath(self.Delete_Confirmation_Yes_xpath).click()

    def manage_user_delete_confirmation_no(self):
        self.driver.find_element_by_xpath(self.Delete_Confirmation_No_xpath).click()

# Function definition to update the user role
    def manage_user_Update_button(self,role_id):
        self.driver.find_element_by_id(self.Click_Update_Button_id).click()
        if role_id==2 :
            self.driver.find_element_by_xpath("//*[@id='updaterole']/option[2]").click()
        elif role_id== 3 :
            self.driver.find_element_by_xpath("//*[@id='updaterole']/option[3]").click()
        elif role_id== 4 :
            self.driver.find_element_by_xpath("//*[@id='updaterole']/option[4]").click()
        elif role_id ==5:
            self.driver.find_element_by_xpath("//*[@id='updaterole']/option[5]").click()
        elif role_id ==6:
            self.driver.find_element_by_xpath("//*[@id='updaterole']/option[6]").click()

# Function definition to Save the update in Update role window  under manage user page of user Module
    def manage_user_update_save(self):
        self.driver.find_element_by_xpath(self.Update_Button_Update_xpath).click()

# Function definition to cancel the update in Update role window  under manage user page of user Module
    def manage_user_update_cancel(self):
        self.driver.find_element_by_xpath(self.Update_Button_Cancel_xpath).click()

# Function definition to add the user under manage user page of user Module
    def manage_user_user_add(self):
        self.manage_user_click()
        time.sleep(2)
        self.manage_user_add_user()

    def manage_user_delete_all_user(self):
        self.manage_user_main_checkbox()
        self.manage_user_delete_user()
        self.manage_user_delete_confirmation_yes()

    def manage_user_update_all_users(self,role_id):
        self.manage_user_main_checkbox()
        self.manage_user_Update_button(role_id)
        self.manage_user_update_save()
