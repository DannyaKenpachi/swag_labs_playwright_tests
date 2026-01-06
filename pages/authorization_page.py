from playwright.sync_api import Page, expect

class AuthorizationPage():
    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator("[data-test=\"username\"]")
        self.password = page.locator("[data-test=\"password\"]")
        self.button_to_login = page.locator("[data-test=\"login-button\"]")
    
    def login(self):
        self.username.fill('standard_user')
        self.password.fill('secret_sauce')
        self.button_to_login.click()
        expect(self.page.locator("[data-test=\"title\"]")).to_have_text('Products')