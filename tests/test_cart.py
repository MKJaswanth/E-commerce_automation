from pages.cart_page import CartPage 
from pages.inventory_page import InventoryPage
from playwright.sync_api import Page , expect
import pytest

class TestCart:

    def test_tc012_add_single_item(self ,logged_in_page : Page):
        inventory = InventoryPage(logged_in_page)
        inventory.add_to_cart("Sauce Labs Backpack")
        expect(inventory.cart_badge).to_have_text("1")

    def test_tc013_add_multtiple_items(self,logged_in_page: Page):
        inventory = InventoryPage(logged_in_page)
        inventory.add_to_cart("Sauce Labs Backpack")
        inventory.add_to_cart("Sauce Labs Bike Light")
        inventory.add_to_cart("Sauce Labs Bolt T-Shirt")
        expect(inventory.cart_badge).to_have_text("3")

    def test_tc014_remove_item_from_cart(self, logged_in_page: Page,  ):
        inventory = InventoryPage(logged_in_page)
        inventory.add_to_cart("Sauce Labs Backpack")
        inventory.go_to_cart()

        cart = CartPage(logged_in_page)
        logged_in_page.locator('[data-test="remove-sauce-labs-backpack"]').click()
        assert cart.get_item_count() == 0
        

    def test_tc015_continue_shopping(self, logged_in_page: Page):
        inventory = InventoryPage(logged_in_page)
        inventory.go_to_cart()

        cart = CartPage(logged_in_page)

        cart.continue_shopping.click()

        expect(inventory.page_title).to_have_text("Products")

    def test_tc016_verify_cart_item_details(self, logged_in_page: Page):
        inventory = InventoryPage(logged_in_page)
        product_name = "Sauce Labs Backpack"
        inventory.add_to_cart("Sauce Labs Backpack")
        inventory.go_to_cart()

        cart_item_name = logged_in_page.locator(".inventory_item_name")
        cart_item_price = logged_in_page.locator(".inventory_item_price")

        expect(cart_item_name).to_have_text(product_name)

        expect(cart_item_price).to_have_text("$29.99")