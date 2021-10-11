from time import sleep
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Cart:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 6)

    def click_cart_button(self):
        '''click on cart icon at the top of the site'''
        self.driver.find_element_by_id('shoppingCartLink').click()

    def product_name_in_mini_cart(self, productNum):
        '''function that returns the product name from the mini cart by index (starts from 1)'''
        return self.driver.find_elements_by_css_selector("h3[class='ng-binding']")[productNum-1].text[:-3]

    def product_price_in_mini_cart(self,productNum):
        '''function that returns the product price from the mini cart by index (starts from 1)'''
        price_mini_cart = (self.driver.find_elements_by_css_selector(".price")[productNum-1].text[1:]).replace(",","")
        return float(price_mini_cart)

    def product_color_in_mini_cart(self,prodNum):
        '''function that returns the product color from the mini cart by index (starts from 1)'''
        return self.driver.find_elements_by_css_selector("label>span.ng-binding")[prodNum-1].text

    def product_quantity_in_mini_cart(self,prodNum):
        '''function that returns the product name from the mini cart by index (starts from 1)'''
        return int(self.driver.find_elements_by_xpath("//*[@id='product']/td[2]/a/label[1]")[prodNum-1].text[5:])

    def total_price_in_cart(self):
        '''function that return total price from cart'''
        total_price = self.driver.find_element_by_css_selector("#shoppingCart>table>tfoot>tr>td[colspan='2']>span[class='roboto-medium ng-binding']").text[1:]
        return float(total_price.replace(",",""))

    def edit_btn_in_cart(self,prodNum):
        '''clicks on edit button inside the cart page'''
        # self.wait.until_not(EC.invisibility_of_element_located((By.CSS_SELECTOR, "a[class='edit ng-scope']")))
        self.driver.find_elements_by_css_selector("a[class='edit ng-scope']")[prodNum].click()

    def quantity_check_in_cart(self,prodNum):
        '''function that returns the quantity from chose product in cart'''
        quantity = self.driver.find_elements_by_css_selector("td[class='smollCell quantityMobile']>label[class='ng-binding']")[prodNum]
        return int(quantity.text)

    def click_checkout_button(self):
        '''click on checkout button'''
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "td[colspan='5']>button[role='button']")))
        self.driver.find_element_by_css_selector("td[colspan='5']>button[role='button']").click()

    def number_of_items_in_mini_cart(self):
        '''returns the number of products in the mini cart'''
        return self.driver.find_element_by_css_selector("#shoppingCartLink > span").text

    def empty_cart_check(self):
        '''functions that returns "Empty cart" from cart'''
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "label[class='center roboto-medium ng-scope']")))
        return self.driver.find_element_by_css_selector("label[class='center roboto-medium ng-scope']").text

    def shopping_cart_written_in_page(self):
        '''function that returns "SHOPPING CART" from cart page'''
        page_title = self.driver.find_element_by_css_selector("[class='select  ng-binding']")
        return page_title.text

    def click_x_button_cart_window(self):
        '''functions that removing product from mini cart'''
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='removeProduct iconCss iconX'")))
        self.driver.find_element_by_css_selector("[class='removeProduct iconCss iconX']").click()

    def products_list_in_cart(self):
        '''function that making list of product names and return it'''
        products_list = self.driver.find_elements_by_css_selector("h3[class='ng-binding']")
        products_list_copy = []
        for i in range(len(products_list)):
            products_list_copy.append(self.driver.find_elements_by_css_selector("h3[class='ng-binding']")[i].text)
        return products_list_copy

    # def empty_orders_check(self):
    #     return self.driver.find_element_by_css_selector("label[class='roboto-bold ng-binding']").text
    #     #functions that checks if the order page is empty
    #
    # def my_orders_page(self):
    #     return self.driver.find_element_by_css_selector("body[class='ng-scope']")



