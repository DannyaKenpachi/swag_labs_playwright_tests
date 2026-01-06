from playwright.sync_api import Page, expect

class CartPage():
    def __init__(self, page: Page):
        self.page = page
        self.checkout = page.locator("[data-test=\"checkout\"]")

    def check_product(self, product: str):
        expect(self.page.locator("[data-test=\"item-4-title-link\"]")).to_have_text(product)

    def buy_product(self):
        self.checkout.click()
        expect(self.page.locator("[data-test=\"title\"]")).to_have_text('Checkout: Your Information')
