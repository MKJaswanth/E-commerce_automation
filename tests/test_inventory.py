import pytest
from playwright.sync_api import Page , expect
from pages.inventory_page import InventoryPage

class TestInventory:
    def test_tc007_inventory_page_loads(self, logged_in_page: Page):
        inventory = InventoryPage(logged_in_page)
        expect(inventory.page_title).to_have_text("Products")
        expect(inventory.sort_dropdown).to_be_visible()
        expect(inventory.cart_icon).to_be_visible()
        expect(inventory.inventory_items).to_have_count(6)
        assert inventory.inventory_items.count() == 6

    def test_tc008_sort_az(self, logged_in_page: Page):
        inventory = InventoryPage(logged_in_page)
        inventory.sort_by("az")
        first_item = inventory.inventory_items.nth(0).locator(".inventory_item_name")
        expect(first_item).to_have_text("Sauce Labs Backpack")

    def test_tc009_sort_price_low_high(self, logged_in_page: Page):
        inventory = InventoryPage(logged_in_page)
        inventory.sort_by("lohi")
        first_item_price = inventory.inventory_items.nth(0).locator(".inventory_item_price")
        expect(first_item_price).to_have_text("$7.99")

    def test_tc010_open_product_detail(self, logged_in_page: Page):

        inventory = InventoryPage(logged_in_page)

        product_name = "Sauce Labs Backpack"

        logged_in_page.locator(f'text={product_name}').click()

        detail_title = logged_in_page.locator(".inventory_details_name")
        expect(detail_title).to_have_text(product_name)

    def test_tc011_verify_product_prices(self, logged_in_page: Page):
        inventory = InventoryPage(logged_in_page)
        prices = logged_in_page.locator(".inventory_item_price").all_inner_texts()

        for price in prices:
            assert '$' in price