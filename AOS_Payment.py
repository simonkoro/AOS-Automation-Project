from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Payment:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 6)

    def click_mastercredit_payment(self):
        '''clicks on mastercredit payment option'''
        self.driver.find_element_by_css_selector("input[name='masterCredit']").click()

    def insert_mastercredit_info(self,cardnumber,cvv,month,year,card_holder):
        '''insert relevant info to mastercredit fields'''
        self.driver.find_element_by_id("creditCard").send_keys(cardnumber)
        self.driver.find_element_by_css_selector("input[name='cvv_number']").send_keys(cvv)
        month_select = Select(self.driver.find_element_by_css_selector("select[name='mmListbox']"))
        month_select.select_by_index(month)
        year_select = Select(self.driver.find_element_by_css_selector("select[name='yyyyListbox']"))
        year_select.select_by_value(f"string:{year}")
        self.driver.find_element_by_css_selector("input[name='cardholder_name']").send_keys(card_holder)

    def click_pay_now(self):
        '''click on pay now at the payment page'''
        # self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "'button[id='pay_now_btn_ManualPayment']'")))
        self.driver.find_element_by_css_selector("button[id='pay_now_btn_ManualPayment']").click()

    def click_next_btn(self):
        '''click on next button at the order page'''
        self.driver.find_element_by_id("next_btn").click()

    def safepay_payment(self,safeusername,safepassword):
        '''enters 'safepay' username and password'''
        # self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='safepay']")))
        # self.driver.find_element_by_css_selector("[name='safepay']").click()
        self.driver.find_element_by_css_selector("[name='safepay_username']").send_keys(safeusername)
        sleep(2)
        self.driver.find_element_by_css_selector("[name='safepay_password']").send_keys(safepassword)
        self.wait.until(EC.element_to_be_clickable((By.ID, 'pay_now_btn_SAFEPAY')))
        self.driver.find_element_by_id('pay_now_btn_SAFEPAY').click()


    def payment_made_check(self):
        '''function that returns "Thanks you for buying" message'''
        return self.driver.find_element_by_css_selector("[class='roboto-regular ng-scope']").text

    def product_name_tag_in_orders(self):
        '''function that return the title "PRODUCT NAME" from my orders page'''
        return self.driver.find_element_by_css_selector("label[translate='PRODUCT_NAME']").text


    # def getting_order_number(self):
    # '''function that returns the order number after payment'''
    #     return self.driver.find_element_by_id("orderNumberLabel").text