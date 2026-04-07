import pytest 
import os 
from playwright.sync_api import Page , sync_playwright , expect
from pages.login_page import LoginPage

BASE_URL = os.getenv("BASE_URL")

class TestLogin:
    def test_tc001_valid_login(self, navigate: Page):

        login = LoginPage(navigate)
        login.login("standard_user","secret_sauce")
        expect(navigate).to_have_url(f"{BASE_URL}/inventory.html")

    def test_tc002_locked_out_user(self, navigate: Page):

        login = LoginPage(navigate)
        login.login("locked_out_user","secret_sauce")
        error = login.get_error_message()
        assert error == "Epic sadface: Sorry, this user has been locked out."
        assert 'locked out' in error.lower()

    def test_tc003_empty_username(self, navigate: Page):

        login = LoginPage(navigate)
        login.login("","secret_sauce")
        error = login.get_error_message()
        assert error == "Epic sadface: Username is required"
        assert 'username is required' in error.lower()
    def test_tc004_empty_password(self, navigate: Page):
        login = LoginPage(navigate)
        login.login("STANDARD_USER","")
        error = login.get_error_message()
        assert error == "Epic sadface: Password is required"
        assert 'password is required' in error.lower()

    def test_tc005_wrong_credentials(self, navigate: Page):

        login = LoginPage(navigate)
        login.login("wrong_user","wrong_pass")
        error = login.get_error_message()
        assert error == "Epic sadface: Username and password do not match any user in this service"
        assert 'do not match' in error.lower()
    
    def test_tc006_logout(self, logged_in_page: Page):
        page = logged_in_page
        page.locator("#react-burger-menu-btn").click()
        page.locator("#logout_sidebar_link").click()
        expect(page).to_have_url(f"{os.getenv('BASE_URL')}/")
