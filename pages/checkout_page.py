from playwright.sync_api import Page
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.first_name = page.locator('[data-test="firstName"]')
        self.last_name = page.locator('[data-test="lastName"]')
        self.zip_code = page.locator('[data-test="postalCode"]')
        self.continue_btn = page.locator('[data-test="continue"]')
        self.finish_btn = page.locator('[data-test="finish"]')
        self.confirm_msg = page.locator(".complete-header")

    def fill_shipping_info(self, first_name: str, last_name: str, zip_code: str):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.zip_code.fill(zip_code)
    

    def click_continue(self):
        self.continue_btn.click()

    def click_finish(self):
        self.finish_btn.click()

    def get_confirmation_message(self) -> str:
        return self.confirm_msg.inner_text()

