from playwright.sync_api import Page
from pages.base_page import BasePage

class InventoryPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page_title = page.locator(".title")
        self.sort_dropdown = page.locator('[data-test="product-sort-container"]')
        self.cart_icon = page.locator(".shopping_cart_link")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.inventory_items = page.locator(".inventory_item")

    def add_to_cart(self, product_name: str):
        btn_id = product_name.lower().replace(" ", "-")
        self.page.locator(f'[data-test="add-to-cart-{btn_id}"]').click()

    def go_to_cart(self):
        self.cart_icon.click()

    def sort_by(self, option: str):
        self.sort_dropdown.select_option(option)