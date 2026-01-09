from playwright.sync_api import Page, expect

class CheckOut():
    def __init__(self, page: Page) -> None:
        self.page = page
        self.firstname = page.locator("[data-test=\"firstName\"]")
        self.lastname = page.locator("[data-test=\"lastName\"]")
        self.postal_code = page.locator("[data-test=\"postalCode\"]")
        self.button_continue = page.locator("[data-test=\"continue\"]")

    def send_data(self):
        self.firstname.fill('Test')
        self.lastname.fill('User')
        self.postal_code.fill('12345')
        self.button_continue.click()
        expect(self.page.locator("[data-test=\"title\"]")).to_have_text('Checkout: Overview')
