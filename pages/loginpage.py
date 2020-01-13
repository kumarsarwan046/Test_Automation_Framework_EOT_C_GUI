class LoginPage():
    def __init__(self, driver):
        self.driver = driver
        self.email_id_textbox_id = "Email"                                                          # Enter EmailId in Main Login page
        self.password_textbox_id = "Password"                                                       # Enter Password in Main Login page
        self.login_xpath = "//*[@id='loginForm']/form/footer/input"

    def enter_email_id(self,email_id):                                                              #Function for entering the Email ID
        self.driver.find_element_by_id(self.email_id_textbox_id).clear()
        self.driver.find_element_by_id(self.email_id_textbox_id).send_keys(email_id)

    def enter_password(self,password):                                                              #Function for entering the password
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_login(self):                                                                          #Function for Clicking on Login Button
        self.driver.find_element_by_xpath(self.login_xpath).click()

    # Function that allows to login in to EOT_C Web, that call multiple function
    def Login(self,email_id,password):
        self.enter_email_id(email_id)                    #Function call to enter the mail id
        self.enter_password(password)                    #Function call to enter the password
        self.click_login()                               #Function call to click on login