from playwright.sync_api import Page, expect

class FinishPage():
    def __init__(self, page: Page) -> None:
        self.page = page
        self.completed_header = page.locator("[data-test=\"complete-header\"]")
        self.completed_text = page.locator("[data-test=\"complete-text\"]")
        self.button_to_home = page.locator("[data-test=\"back-to-products\"]")

    def check_finish(self):
        expect(self.completed_header).to_have_text('Thank you for your order!')
        expect(self.completed_text).to_have_text('Your order has been dispatched, and will arrive just as fast as the pony can get there!')

    def back_to_home(self):
        self.button_to_home.click()
        expect(self.page.locator("[data-test=\"title\"]")).to_have_text('Products')