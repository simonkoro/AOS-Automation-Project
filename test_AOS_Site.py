from unittest import TestCase
from selenium import webdriver
from AutomationProject.AOS_Cart import Cart
from AutomationProject.AOS_Payment import Payment
from AutomationProject.AOS_User import User
from AutomationProject.AOS_Selecting_Proccess import Selecting
from time import sleep
from openpyxl import load_workbook
workbook = load_workbook("D:\Downloads\SeleniumProject.xlsx")
cell = workbook.active


class AosTest(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\Selenium\chromedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.advantageonlineshopping.com/#/")
        self.driver.maximize_window()
        sleep(2)
        self.driver.refresh()
        sleep(2)
        self.driver.refresh()
        self.user = User(self.driver)
        self.payment = Payment(self.driver)
        self.cart = Cart(self.driver)
        self.shopping = Selecting(self.driver)
        self.if_passed = False

    def test_1_check_correct_quantity(self):
        '''test that checks if the quantity in mini-cart is right'''
        testID = "C"
        product1_category = cell["c2"].value
        product1_id = int(cell["c3"].value)
        product1_quantity = int(cell["c4"].value)
        product1_color = cell["c5"].value

        product2_category = cell["c6"].value
        product2_id = int(cell["c7"].value)
        product2_quantity = int(cell["c8"].value)
        product2_color = cell["c9"].value

        self.shopping.category_opening(product1_category)
        self.shopping.select_product_and_color(product1_id,product1_color)
        self.shopping.select_quantity_click(product1_quantity)
        self.shopping.add_to_cart()
        quantity1 = self.shopping.get_product_quantity()
        self.shopping.click_home_button()
        self.shopping.category_opening(product2_category)
        self.shopping.select_product_and_color(product2_id,product2_color)
        self.shopping.select_quantity_click(product2_quantity)
        self.shopping.add_to_cart()
        quantity2 = self.shopping.get_product_quantity()
        cart_quantity = self.cart.number_of_items_in_mini_cart()
        self.assertEqual(quantity1 + quantity2, int(cart_quantity))
        self.if_passed = True
        self.check_test(testID,self.if_passed)


    def test_2_check_correct_cart_info(self):
        '''test that checks if the products we chose added correctly to cart'''
        testID = "D"
        product1_category = cell["d2"].value
        product1_id = int(cell["d3"].value)
        product1_quantity = int(cell["d4"].value)
        product1_color = cell["d5"].value
        self.shopping.category_opening(product1_category)
        self.shopping.select_product_and_color(product1_id,product1_color)
        self.shopping.select_quantity_click(product1_quantity)
        product1_name = self.shopping.get_product_name()
        product1_price = self.shopping.get_product_price()
        product1_quantity = self.shopping.get_product_quantity()
        # sleep(2)
        self.shopping.add_to_cart()
        self.shopping.click_home_button()

        product2_category = cell["d6"].value
        product2_id = int(cell["d7"].value)
        product2_quantity = int(cell["d8"].value)
        product2_color = cell["d9"].value
        self.shopping.category_opening(product2_category)
        self.shopping.select_product_and_color(product2_id,product2_color)
        self.shopping.select_quantity_click(product2_quantity)
        product2_name = self.shopping.get_product_name()
        product2_price = self.shopping.get_product_price()
        product2_quantity = self.shopping.get_product_quantity()
        # sleep(2)
        self.shopping.add_to_cart()
        self.shopping.click_home_button()

        product3_category = cell["d10"].value
        product3_id = int(cell["d11"].value)
        product3_quantity = int(cell["d12"].value)
        product3_color = cell["d13"].value
        self.shopping.category_opening(product3_category)
        self.shopping.select_product_and_color(product3_id,product3_color)
        self.shopping.select_quantity_click(product3_quantity)
        product3_name = self.shopping.get_product_name()
        product3_price = self.shopping.get_product_price()
        product3_quantity = self.shopping.get_product_quantity()
        # sleep(2)
        self.shopping.add_to_cart()

        self.assertIn(self.cart.product_name_in_mini_cart(3),product1_name)
        self.assertEqual(product1_price*product1_quantity,self.cart.product_price_in_mini_cart(3))
        self.assertTrue(product1_color,self.cart.product_color_in_mini_cart(3))
        self.assertEqual(product1_quantity,self.cart.product_quantity_in_mini_cart(3))
        self.assertIn(self.cart.product_name_in_mini_cart(2),product2_name)
        self.assertEqual(product2_price*product2_quantity,self.cart.product_price_in_mini_cart(2))
        self.assertTrue(product2_color,self.cart.product_color_in_mini_cart(2))
        self.assertEqual(product2_quantity,self.cart.product_quantity_in_mini_cart(2))
        self.assertIn(self.cart.product_name_in_mini_cart(1),product3_name)
        self.assertEqual(product3_price*product3_quantity,self.cart.product_price_in_mini_cart(1))
        self.assertTrue(product3_color,self.cart.product_color_in_mini_cart(1))
        self.assertEqual(product3_quantity,self.cart.product_quantity_in_mini_cart(1))
        self.if_passed = True
        self.check_test(testID,self.if_passed)

    def test_3_check_removed_product(self):
        '''test that removing item and checks if it removed from cart'''
        testID = "E"
        product1_category = cell["e2"].value
        product1_id = int(cell["e3"].value)
        product1_quantity = int(cell["e4"].value)
        product1_color = cell["e5"].value

        product2_category = cell["e6"].value
        product2_id = int(cell["e7"].value)
        product2_quantity = int(cell["e8"].value)
        product2_color = cell["e9"].value

        product3_category = cell["e10"].value
        product3_id = int(cell["e11"].value)
        product3_quantity = int(cell["e12"].value)
        product3_color = cell["e13"].value
        self.shopping.adding_products_to_cart_proccess(product1_category,
                                                       product1_id,
                                                       product1_color,
                                                       product1_quantity)
        # sleep(2)
        self.shopping.adding_products_to_cart_proccess(product2_category, product2_id, product2_color,
                                                       product2_quantity)
        # sleep(2)
        self.shopping.category_opening(product3_category)
        self.shopping.select_product_and_color(product3_id, product3_color)
        canceled_product_name = self.shopping.get_product_name()
        self.shopping.select_quantity_click(product3_quantity)
        self.shopping.add_to_cart()
        self.shopping.click_home_button()
        # sleep(2)
        self.cart.click_x_button_cart_window()
        self.cart.click_cart_button()
        # sleep(5)
        self.assertNotIn(canceled_product_name, self.cart.products_list_in_cart())
        cart_quantity = self.cart.number_of_items_in_mini_cart()
        self.assertEqual(product1_quantity + product2_quantity, int(cart_quantity))
        self.if_passed = True
        self.check_test(testID,self.if_passed)

    def test_4_shopping_cart_page(self):
        '''test that checks if we are on the cart page'''
        testID = "F"
        product1_category = cell["f2"].value
        product1_id = int(cell["f3"].value)
        product1_quantity = int(cell["f4"].value)
        product1_color = cell["f5"].value

        self.shopping.category_opening(product1_category)
        self.shopping.select_product_and_color(product1_id, product1_color)
        self.shopping.select_quantity_click(product1_quantity)
        self.shopping.add_to_cart()
        self.cart.click_cart_button()
        # sleep(5)
        self.assertEqual(self.cart.shopping_cart_written_in_page(), 'SHOPPING CART')
        self.if_passed = True
        self.check_test(testID,self.if_passed)

    def test_5_total_price_check(self):
        '''test that checks if all the product's prices combined right to total price'''
        testID = "G"
        product1_category = cell["g2"].value
        product1_id = int(cell["g3"].value)
        product1_quantity = int(cell["g4"].value)
        product1_color = cell["g5"].value
        self.shopping.category_opening(product1_category)
        self.shopping.select_product_and_color(product1_id, product1_color)
        self.shopping.select_quantity_click(product1_quantity)
        product1_name = self.shopping.get_product_name()
        product1_price = self.shopping.get_product_price()
        product1_quantity = self.shopping.get_product_quantity()
        # sleep(2)
        self.shopping.add_to_cart()
        self.shopping.click_home_button()

        product2_category = cell["g6"].value
        product2_id = int(cell["g7"].value)
        product2_quantity = int(cell["g8"].value)
        product2_color = cell["g9"].value
        self.shopping.category_opening(product2_category)
        self.shopping.select_product_and_color(product2_id, product2_color)
        self.shopping.select_quantity_click(product2_quantity)
        product2_name = self.shopping.get_product_name()
        product2_price = self.shopping.get_product_price()
        product2_quantity = self.shopping.get_product_quantity()
        # sleep(2)
        self.shopping.add_to_cart()
        self.shopping.click_home_button()

        product3_category = cell["g10"].value
        product3_id = int(cell["g11"].value)
        product3_quantity = int(cell["g12"].value)
        product3_color = cell["g13"].value
        self.shopping.category_opening(product3_category)
        self.shopping.select_product_and_color(product3_id, product3_color)
        self.shopping.select_quantity_click(product3_quantity)
        product3_name = self.shopping.get_product_name()
        product3_price = self.shopping.get_product_price()
        product3_quantity = self.shopping.get_product_quantity()
        # sleep(2)
        self.shopping.add_to_cart()
        self.cart.click_cart_button()


        total_product1 = product1_price*product1_quantity
        total_product2 = product2_price*product2_quantity
        total_product3 = product3_price*product3_quantity
        print(product1_name)
        print("Price: $", product1_price)
        print("QTY: ", product1_quantity)
        print(product2_name)
        print("Price: $", product2_price)
        print("QTY: ", product2_quantity)
        print(product3_name)
        print("Price: $", product3_price)
        print("QTY: ", product3_quantity)
        self.assertEqual(total_product1+total_product2+total_product3, self.cart.total_price_in_cart())
        self.if_passed = True
        self.check_test(testID,self.if_passed)

    def test_6_changes_in_cart(self):
        '''test that checks if after editing the quntity the quantity changed'''
        testID = "H"
        product1_category = cell["h2"].value
        product1_id = int(cell["h3"].value)
        product1_quantity = int(cell["h4"].value)
        product1_color = cell["h5"].value
        self.shopping.category_opening(product1_category)
        self.shopping.select_product_and_color(product1_id, product1_color)
        self.shopping.select_quantity_click(product1_quantity)
        self.shopping.add_to_cart()
        self.shopping.click_home_button()

        product2_category = cell["h6"].value
        product2_id = int(cell["h7"].value)
        product2_quantity = int(cell["h8"].value)
        product2_color = cell["h9"].value
        self.shopping.category_opening(product2_category)
        self.shopping.select_product_and_color(product2_id, product2_color)
        self.shopping.select_quantity_click(product2_quantity)
        self.shopping.add_to_cart()
        self.cart.click_cart_button()

        sleep(5)
        self.cart.edit_btn_in_cart(0)
        self.shopping.select_quantity_click(6)
        product1_quantity = self.shopping.get_product_quantity()
        self.shopping.add_to_cart()
        self.cart.click_cart_button()
        sleep(5)
        self.cart.edit_btn_in_cart(1)
        self.shopping.select_quantity_click(3)
        product2_quantity = self.shopping.get_product_quantity()
        self.cart.click_cart_button()
        # sleep(6)

        self.assertEqual(product1_quantity,self.cart.quantity_check_in_cart(0))
        self.assertEqual(product2_quantity,self.cart.quantity_check_in_cart(1))
        self.if_passed = True
        self.check_test(testID,self.if_passed)

    def test_7_category_and_home_page(self):
        '''test that checks category page and home page'''
        testID = "I"
        product1_category = cell["i2"].value
        product1_id = int(cell["i3"].value)
        product1_quantity = int(cell["i4"].value)
        product1_color = cell["i5"].value

        self.shopping.category_opening(product1_category)
        self.shopping.select_product_and_color(product1_id,product1_color)
        self.shopping.select_quantity_click(product1_quantity)
        self.shopping.add_to_cart()
        self.driver.back()
        self.assertEqual(self.shopping.check_tablet_category_title(),'TABLETS')
        self.driver.back()
        self.assertEqual(self.shopping.check_homepage_specialoffer(),'SPECIAL OFFER')
        self.cart.click_cart_button()
        self.if_passed = True
        self.check_test(testID,self.if_passed)

    def test_8_empty_cart_and_order_in_orders_safepay(self):
        '''test that checks if the the order paid,the cart is empty and the order in orders after paying with safepay'''
        testID = "J"
        product1_category = cell["j2"].value
        product1_id = int(cell["j3"].value)
        product1_quantity = int(cell["j4"].value)
        product1_color = cell["j5"].value

        product2_category = cell["j6"].value
        product2_id = int(cell["j7"].value)
        product2_quantity = int(cell["j8"].value)
        product2_color = cell["j9"].value

        username = cell["j16"].value
        password = cell["j17"].value
        email = cell["j18"].value

        safepay_username = cell["j19"].value
        safepay_password = cell["j20"].value

        self.shopping.adding_products_to_cart_proccess(product1_category, product1_id, product1_color,
                                                       product1_quantity)
        self.shopping.adding_products_to_cart_proccess(product2_category, product2_id, product2_color,
                                                       product2_quantity)
        self.cart.click_cart_button()
        self.cart.click_checkout_button()
        self.user.click_registration_button()
        # sleep(1)
        self.user.insert_username("simon159827")
        self.user.insert_email(email)
        self.user.insert_password(password)
        self.user.confirm_password(password)
        self.user.check_i_agree_checkbox_and_click_register()
        # sleep(1)
        self.user.click_next_after_create_user()
        # sleep(4)
        self.payment.safepay_payment(safepay_username, safepay_password)
        sleep(2)
        self.assertEqual(self.payment.payment_made_check(), "Thank you for buying with Advantage")
        # sleep(4)
        self.user.click_my_orders()
        # sleep(3)
        self.assertEqual("PRODUCT NAME", self.payment.product_name_tag_in_orders())
        self.cart.click_cart_button()
        self.assertEqual(self.cart.empty_cart_check(), "Your shopping cart is empty")
        self.if_passed = True
        self.check_test(testID, self.if_passed)


    def test_9_empty_cart_and_order_in_orders_creditcart(self):
        '''test that checks if the cart is empty and the order in orders after paying with creditcard'''
        testID = "K"
        product1_category = cell["k2"].value
        product1_id = int(cell["k3"].value)
        product1_quantity = int(cell["k4"].value)
        product1_color = cell["k5"].value
        username = cell["k14"].value
        password = cell["k15"].value
        cardnumber = int(cell["k21"].value)
        cvv = int(cell["k22"].value)
        year = int(cell["k23"].value)
        month = int(cell["k24"].value)
        card_holder = cell["k25"].value

        self.shopping.category_opening(product1_category)
        self.shopping.select_product_and_color(product1_id, product1_color)
        self.shopping.select_quantity_click(product1_quantity)
        self.shopping.add_to_cart()
        self.cart.click_cart_button()
        self.cart.click_checkout_button()

        self.user.user_login_from_checkout(username,password)
        self.payment.click_next_btn()
        self.payment.click_mastercredit_payment()
        self.payment.insert_mastercredit_info(cardnumber,cvv,month,year,card_holder)
        sleep(2)
        self.payment.click_pay_now()
        sleep(2)
        self.user.click_my_orders()
        sleep(1)
        self.assertEqual("PRODUCT NAME", self.payment.product_name_tag_in_orders())
        self.cart.click_cart_button()
        self.assertEqual(self.cart.empty_cart_check(), "Your shopping cart is empty")
        self.if_passed = True
        self.check_test(testID,self.if_passed)

    def test_10_check_login_logout(self):
        '''test that checks the log out process'''
        testID = "L"
        username = cell["l14"].value
        password = cell["l15"].value
        self.user.login(username, password)
        sleep(5)
        self.assertEqual(self.user.after_login_check(), username)
        self.user.logout()
        sleep(5)
        self.assertEqual(self.shopping.check_homepage_specialoffer(), 'SPECIAL OFFER')
        sleep(4)
        self.assertEqual(self.user.check_logout_succeed(), 'REMEMBER ME')
        self.if_passed = True
        self.check_test(testID,self.if_passed)

    def tearDown(self):
        self.shopping.click_home_button()
        self.driver.close()


    def check_test(self, testID, if_passed=False):
        if if_passed:
            cell[f"{testID}26"] = "V"
            workbook.save(filename="D:\Downloads\SeleniumProject.xlsx")
        else:
            cell[f"{testID}26"] = "X"
            workbook.save(filename="D:\Downloads\SeleniumProject.xlsx")