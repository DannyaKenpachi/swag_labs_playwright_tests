from playwright.sync_api import Page

class MainPage():
    def __init__(self, page: Page):
        self.page = page
        self.cart = page.locator("[data-test=\"shopping-cart-link\"]")
    
    def add_to_cart(self, product: str):
        card_of_product = self.page.locator("[data-test=\"inventory-item-description\"]").filter(has_text=product)
        button_for_add_to_cart = card_of_product.get_by_role('button', name='Add to cart')
        button_for_add_to_cart.click()

    def open_cart(self):
        self.cart.click()