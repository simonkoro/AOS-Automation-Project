from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class User:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 6)

    def user_login_from_checkout(self,username,password):
        '''login procces from the checkout page'''
        self.driver.find_element_by_css_selector("[name='usernameInOrderPayment']").send_keys(username)
        self.driver.find_element_by_css_selector("[name='passwordInOrderPayment']").send_keys(password)
        self.driver.find_element_by_id("login_btnundefined").click()

    def click_my_orders(self):
        '''clicks on my orders page'''
        self.driver.find_element_by_id("menuUserLink").click()
        sleep(2)
        self.driver.find_element_by_css_selector("div[id='loginMiniTitle']>label[translate='My_Orders']").click()

    def click_registration_button(self):
        '''clicks on register button after choosing order'''
        self.wait.until(EC.element_to_be_clickable((By.ID, 'registration_btnundefined')))
        self.driver.find_element_by_id('registration_btnundefined').click()

    def insert_username(self, username):
        '''enters username'''
        self.driver.find_element_by_css_selector("[name='usernameRegisterPage']").send_keys(username)

    def insert_email(self, email):
        '''enters email'''
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[name = 'emailRegisterPage']")))
        self.driver.find_element_by_css_selector("[name = 'emailRegisterPage']").send_keys(email)

    def insert_password(self, password):
        '''enters password'''
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='passwordRegisterPage']")))
        self.driver.find_element_by_css_selector("[name='passwordRegisterPage']").send_keys(password)

    def confirm_password(self, password):
        '''enters password second time'''
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[name = 'confirm_passwordRegisterPage']")))
        self.driver.find_element_by_css_selector("[name = 'confirm_passwordRegisterPage']").send_keys(password)

    def check_i_agree_checkbox_and_click_register(self):
        '''mark "i agree" and clicks on register'''
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='i_agree']")))
        self.driver.find_element_by_css_selector("[name='i_agree']").click()
        self.wait.until(EC.element_to_be_clickable((By.ID, 'register_btnundefined')))
        self.driver.find_element_by_id('register_btnundefined').click()

    def click_next_after_create_user(self):
        '''clicks next after user creation'''
        self.wait.until(EC.element_to_be_clickable((By.ID, 'next_btn')))
        self.driver.find_element_by_id('next_btn').click()

    def login(self,username,password):
        '''function that doing all the login procces'''
        self.wait.until(EC.element_to_be_clickable((By.ID, 'menuUser')))
        self.driver.find_element_by_id('menuUser').click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[name = 'username']")))
        self.driver.find_element_by_css_selector("[name = 'username']").send_keys(username)
        self.driver.find_element_by_css_selector("[name='password']").send_keys(password)
        self.wait.until(EC.element_to_be_clickable((By.ID, 'sign_in_btnundefined')))
        sleep(5)
        self.driver.find_element_by_id('sign_in_btnundefined').click()

    def after_login_check(self):
        '''function that returns the username on top of the site'''
        self.wait.until(EC.element_to_be_clickable((By.ID, 'menuUserSVGPath')))
        return self.driver.find_element_by_css_selector("[id='menuUserLink']>span").text

    def logout(self):
        '''function that logging out from the site'''
        self.wait.until(EC.element_to_be_clickable((By.ID, 'menuUserLink')))
        self.driver.find_element_by_id('menuUserLink').click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[ng-click='signOut($event)']")))
        self.driver.find_element_by_css_selector("[ng-click='signOut($event)']").click()

    def check_logout_succeed(self):
        '''function that return "remember me" to check if user logged out'''
        self.wait.until(EC.element_to_be_clickable((By.ID, 'menuUser')))
        self.driver.find_element_by_id('menuUser').click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[translate='REMEMBER_ME']")))
        remember_me = self.driver.find_element_by_css_selector("[translate='REMEMBER_ME']").text
        return remember_me

    # def order_num_in_orders(self):
    #     # self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div>label[class='left ng-binding']")))
    #     # return self.driver.find_element_by_css_selector("div>label[class='left ng-binding']").text
    #     return self.driver.find_element_by_css_selector("div>label[class='left ng-binding']").text