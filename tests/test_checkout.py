import pytest
from playwright.sync_api import Page , expect
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

class TestCheckout:
    def test_tc017_complete_checkout(self, logged_in_page: Page):
        inventory = InventoryPage(logged_in_page)
        inventory.add_to_cart('sauce labs backpack')
        inventory.go_to_cart()

        cart = CartPage(logged_in_page)
        cart.checkout_button.click()

        checkout = CheckoutPage(logged_in_page)
        checkout.fill_shipping_info("John", "Doe", "12345")
        checkout.click_continue()
        checkout.click_finish()

        msg = checkout.get_confirmation_message()
        assert msg == "Thank you for your order!" in msg

    def test_tc018_checkout_empty_firstname(self, logged_in_page: Page, ):
        inventory = InventoryPage(logged_in_page)
        inventory.add_to_cart('sauce labs backpack')
        inventory.go_to_cart()

        cart = CartPage(logged_in_page)

        cart.checkout_button.click()

        checkout = CheckoutPage(logged_in_page)
        checkout.fill_shipping_info("", "Doe", "12345")
        checkout.click_continue()

        error_msg = logged_in_page.locator('[data-test="error"]').inner_text()
        assert error_msg == "Error: First Name is required" in error_msg

    def test_tc019_checkout_empty_lastname(self, logged_in_page: Page, ):
        inventory = InventoryPage(logged_in_page)
        inventory.add_to_cart('sauce labs backpack')
        inventory.go_to_cart()

        cart = CartPage(logged_in_page)

        cart.checkout_button.click()

        checkout = CheckoutPage(logged_in_page)
        checkout.fill_shipping_info("John", "", "12345")
        checkout.click_continue()

        error_msg = logged_in_page.locator('[data-test="error"]').inner_text()
        assert error_msg == "Error: Last Name is required" in error_msg


    def test_tc020_checkout_empty_zipcode(self, logged_in_page: Page, ):
        inventory = InventoryPage(logged_in_page)
        inventory.add_to_cart('sauce labs backpack')
        inventory.go_to_cart()

        cart = CartPage(logged_in_page)

        cart.checkout_button.click()

        checkout = CheckoutPage(logged_in_page)
        checkout.fill_shipping_info("John", "Doe", "")
        checkout.click_continue()

        error_msg = logged_in_page.locator('[data-test="error"]').inner_text()        
        assert error_msg == "Error: Postal Code is required" in error_msg   

    def test_tc021_verify_total_calculation(self, logged_in_page: Page):
        inventory = InventoryPage(logged_in_page)
        inventory.add_to_cart('sauce labs backpack')
        inventory.add_to_cart('sauce labs bike light')
        inventory.go_to_cart()

        cart = CartPage(logged_in_page)
        cart.checkout_button.click()

        checkout = CheckoutPage(logged_in_page)
        checkout.fill_shipping_info("John", "Doe", "12345")
        checkout.click_continue()

        item_prices = logged_in_page.locator(".inventory_item_price")
        total_price = 0.0
        for i in range(item_prices.count()):
            price_text = item_prices.nth(i).inner_text().replace("$", "")
            total_price += float(price_text)

        tax = total_price * 0.08
        expected_total = total_price + tax

        displayed_total = logged_in_page.locator(".summary_total_label").inner_text()
        displayed_total_value = float(displayed_total.replace("Total: $", ""))

        assert abs(displayed_total_value - expected_total) < 0.01, f"Expected total {expected_total}, but got {displayed_total_value}"