from pages.authorization_page import AuthorizationPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckOut
from pages.confirmation_page import ConfirmationPage
from pages.finish_page import FinishPage
import pytest

@pytest.fixture
def authorization_page(page):
    return AuthorizationPage(page)

@pytest.fixture
def main_page(page):
    return MainPage(page)

@pytest.fixture
def cart_page(page):
    return CartPage(page)

@pytest.fixture
def checkout_page(page):
    return CheckOut(page)

@pytest.fixture
def confirmation_page(page):
    return ConfirmationPage(page)

@pytest.fixture
def finish_page(page):
    return FinishPage(page)
