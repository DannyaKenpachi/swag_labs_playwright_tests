import pytest
import allure

@allure.feature('Покупка "Sauce Labs Backpack"')
def test_buy_product(authorization_page, main_page, cart_page, checkout_page, confirmation_page, finish_page):
    with allure.step('Авторизация'):
        authorization_page.login()

    with allure.step('Покупка товара'):
        main_page.add_to_cart('Sauce Labs Backpack')

    with allure.step('Переход в корзину'):    
        main_page.open_cart()
        cart_page.check_product('Sauce Labs Backpack')
    
    with allure.step('Заполнение данных'):
        cart_page.buy_product()
        checkout_page.send_data()

    with allure.step('Подтверждение покупки'):
        confirmation_page.confirmation_order('Sauce Labs Backpack')
        finish_page.check_finish()
        
    with allure.step('Возвращение обратно на главную страницу'):    
        finish_page.back_to_home()