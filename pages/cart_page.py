from playwright.sync_api import Page
from pages.base_page import BasePage 

class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.checkout_button = page.locator('[data-test="checkout"]')
        self.continue_shopping = page.locator('[data-test="continue-shopping"]')
        self.cart_items = page.locator(".cart_item")

    def proceed_to_checkout(self):
        self.checkout_button.click()

    def get_item_count(self) -> int:

        return self.cart_items.count()
        