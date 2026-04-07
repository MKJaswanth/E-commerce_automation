from playwright.sync_api import sync_playwright 
from pages.base_page import BasePage
from playwright.sync_api import Page

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.username_field = page.locator("#user-name")
        self.password_field = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator("[data-test='error']")

    def login(self , username: str, password: str):
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()

    def get_error_message(self) -> str:
        return self.error_message.text_content()