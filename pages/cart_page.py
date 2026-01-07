from playwright.sync_api import Page, expect

class CartPage():
    def __init__(self, page: Page) -> None:
        self.page = page
        self.checkout = page.locator("[data-test=\"checkout\"]")

    def check_product(self, product: str):
        expect(self.page.locator("[data-test=\"inventory-item\"]").filter(has_text=product)).to_be_visible()

    def buy_product(self):
        self.checkout.click()
        expect(self.page.locator("[data-test=\"title\"]")).to_have_text('Checkout: Your Information')
