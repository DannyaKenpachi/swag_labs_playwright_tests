from playwright.sync_api import Page, expect

class ConfirmationPage():
    def __init__(self, page: Page) -> None:
        self.page = page
        self.button_finish = page.locator("[data-test=\"finish\"]")

    def confirmation_order(self, product):
        expect(self.page.locator("[data-test=\"inventory-item\"]").filter(has_text=product)).to_be_visible()
        self.button_finish.click()
        expect(self.page.locator("[data-test=\"title\"]")).to_have_text('Checkout: Complete!')
