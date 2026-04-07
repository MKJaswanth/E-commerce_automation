import pytest
import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
from streamlit import Page
from pages.login_page import LoginPage
load_dotenv()

BASE_URL = os.getenv("BASE_URL","https://saucedemo.com")

@pytest.fixture(scope="function")
def navigate(page: Page):
    page.goto(BASE_URL)
    yield page 


@pytest.fixture(scope="function")
def logged_in_page(page: Page):
    page.goto(BASE_URL)
    login = LoginPage(page)
    login.login(os.getenv("STANDARD_USER"), os.getenv("PASSWORD"))
    yield page

    