import pytest
import allure

def test_buy_product(authorization_page, main_page, cart_page, checkout_page, confirmation_page, finish_page):
    authorization_page.login()

    main_page.add_to_cart('Sauce Labs Backpack')
    main_page.open_cart()

    cart_page.check_product('Sauce Labs Backpack')
    cart_page.buy_product()

    checkout_page.send_data()

    confirmation_page.confirmation_order('Sauce Labs Backpack')

    finish_page.check_finish()
    finish_page.back_to_home()