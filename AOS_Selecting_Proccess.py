from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Selecting:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 6)

    def category_opening(self, category):
        '''function that open category'''
        self.driver.find_element_by_css_selector(f"div[a-sec-back-img='{category}']").click()

    def select_product_and_color(self, id,color):
        '''function that choosing product and color'''
        rabbit = [12,14,27,33,26,31,34,16,17,18,19,20,6,7,8,9]
        bunny = [15,29,28,30,32,1,2,3,4,5,10,11,21,22,23,24,25]
        self.wait.until(EC.element_to_be_clickable((By.ID, id)))
        self.driver.find_element_by_id(id).click()
        if id in rabbit :
            self.driver.find_element_by_css_selector(f"span[title ='{color}'][id ='rabbit']").click()
        if id in bunny:
            self.driver.find_element_by_css_selector(f"span[title ='{color}'][id ='bunny']").click()

    def select_quantity_click(self, quantity):
        '''function that selecting quantity'''
        self.driver.find_element_by_css_selector("[name='quantity']").click()
        self.driver.find_element_by_css_selector("[name='quantity']").send_keys(quantity)

    def add_to_cart(self):
        '''adding product to cart button'''
        # self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='save_to_cart']")))
        self.driver.find_element_by_css_selector("[name='save_to_cart']").click()

    def click_home_button(self):
        '''function that click on the main logo site and return to home page'''
        # self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[translate='HOME']")))
        self.driver.find_element_by_css_selector("[translate='HOME']").click()

    def adding_products_to_cart_proccess(self, category, id, color, quantity):
        '''function that doing all the process of adding product to cart'''
        self.category_opening(category)
        self.select_product_and_color(id,color)
        self.select_quantity_click(quantity)
        self.add_to_cart()
        self.click_home_button()

    def get_product_name(self):
        '''function that returns the product name from product page'''
        return self.driver.find_element_by_css_selector("#Description>.roboto-regular").text

    def get_product_quantity(self):
        '''function that returns the product quantity from product page'''
        return int(self.driver.find_element_by_css_selector("div>input[name='quantity']").get_attribute("value"))

    def get_product_price(self):
        '''function that returns the product price from product page'''
        product_price = (self.driver.find_element_by_css_selector("#Description>h2.roboto-thin").text[1:]).replace(",","")
        return float(product_price)

    def check_tablet_category_title(self):
        '''function that returns the title of the chosen category'''
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'categoryTitle')))
        tablets_title = self.driver.find_element_by_class_name('categoryTitle')
        return tablets_title.text

    def check_homepage_specialoffer(self):
        '''function that check if the user on the main page by "SPEACIAL OFFER" text'''
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h3[translate='SPACIAL_OFFER']")))
        special_offer_title = self.driver.find_element_by_css_selector("h3[translate='SPACIAL_OFFER']")
        return special_offer_title.text