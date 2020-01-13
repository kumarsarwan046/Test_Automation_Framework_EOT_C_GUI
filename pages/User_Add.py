import time
class Add_user():
    def __init__(self,driver):
        self.driver = driver
        self.full_name_id = "FullName"                                      # id for full name field of the user
        self.email_id = "Email"                                             # id of email id field
        self.PhoneNumber_id = "PhoneNumber"                                 # id of phone number field
        self.password_id = "Password"                                       # id of password field
        self.ConfirmPassword_id = "ConfirmPassword"                         # id of confirm password field
        self.select_role_id = "//*[@id='user_role']"                        # id of select role id field
        self.sisa_client_manager_xpath = "//*[@id='user_role']/option[2]"   # xpath of client manager role
        self.sisa_client_consultant_xpath = "//*[@id='user_role']/option[3]"    # xpath of consultant role
        self.admin_xpath = "//*[@id='user_role']/option[4]"                 # xpath of admin role
        self.general_user_xpath = "//*[@id='user_role']/option[5]"          # xpath of general user role
        self.manager_xpath = "//*[@id='user_role']/option[6]"               # xpath of manager role
        self.select_company_id = "select2-chosen-1"                         # xpath for selecting the company id
        self.SISA_Company_xpath = "/html/body/div[8]/ul/li[2]/div"          # xpath of SISA company
        self.save_button_id = "btnSave"                                     # xpath of save button
        self.cancel_button_xpath = "//*[@id='wid-id-4']/div/div[8]/div/button"  # xpath of cancel button
        self.edit_upate_id = "btnUpdate"


# Function definition for entering the user name under add user page of manage user module
    def add_user_enter_user_name(self,user_name):
        self.driver.find_element_by_id(self.full_name_id).send_keys(user_name)
        time.sleep(3)

# Function definition for entering the emailid under add user page of manage user module
    def add_user_enter_email_id(self,email_id):
        self.driver.find_element_by_id(self.email_id).clear()
        self.driver.find_element_by_id(self.email_id).send_keys(email_id)

# Function definition for entering the phone number under add user page of manage user module
    def add_user_enter_phone_number(self,phone_number):
        self.driver.find_element_by_id(self.PhoneNumber_id).send_keys(phone_number)

# Function definition for entering the password under add user page of manage user module
    def add_user_enter_password(self,password):
        self.driver.find_element_by_id(self.password_id).send_keys(password)

# Function definition for entering the confirm password under add user page of manage user module
    def add_user_enter_confirm_password(self,confirm_password):
        self.driver.find_element_by_id(self.ConfirmPassword_id).send_keys(confirm_password)

# Function definition for selecting the user role under add user page of manage user module
    def add_user_select_user_role(self,role):
        self.driver.find_element_by_xpath(self.select_role_id).click()
        if role ==2 :
            self.driver.find_element_by_xpath(self.sisa_client_manager_xpath).click()
        elif role == 3 :
            self.driver.find_element_by_xpath(self.sisa_client_consultant_xpath).click()
        elif role ==4:
            self.driver.find_element_by_xpath(self.admin_xpath).click()
        elif role ==5:
            self.driver.find_element_by_xpath(self.general_user_xpath).click()
        elif role ==6:
            self.driver.find_element_by_xpath(self.manager_xpath).click()

# Function definition for selecting the company under add user page of manage user module
    #def add_user_select_company(self):
    #self.driver.find_element_by_id(self.select_company_id).click()                    EOT_C GUI
    #self.driver.find_element_by_xpath("/html/body/div[8]/ul/li[2]/div").click()       EOT_C GUI

#EOTS
    def add_user_select_company(self):
        self.driver.find_element_by_id(self.select_company_id).click()
        self.driver.find_element_by_id("s2id_autogen1_search").send_keys("SISA KRUTHI (C-0010080)")
        #self.driver.find_element_by_xpath("//*[@id='select2-result-label-217']").click()  # EOT_C GUI
        self.driver.find_element_by_xpath("//*[@id='select2-result-label-152']").click()
# Function definition for clicking save button under add user page of manage user module
    def add_user_click_save(self):
        self.driver.find_element_by_id(self.save_button_id).click()

# Function definition for clicking cancel button under add user page of manage user module
    def add_user_click_cancel(self):
        self.driver.find_element_by_xpath(self.cancel_button_xpath).click()

    def add_user_edit_update(self):
        self.driver.find_element_by_id(self.edit_upate_id).click()

# Function definition to add the user ,that call multiple function
    def add_user(self,user_name,email_id,phone_number,password,confirm_password,role):
        self.add_user_enter_user_name(user_name)                         # Function call to enter the user name
        self.add_user_enter_email_id(email_id)                           # Function call to enter the emailid
        self.add_user_enter_phone_number(phone_number)                   # Function call to enter the phone number
        self.add_user_enter_password(password)                           # Function call to enter the password
        self.add_user_enter_confirm_password(confirm_password)           # Function call to enter the confirm password
        self.add_user_select_user_role(role)                             # Function call for selecting the user
        self.add_user_select_company()                                   # Function call for selecting the company
        self.add_user_click_save()                                       # Function call to save the added user