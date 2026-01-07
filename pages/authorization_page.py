from playwright.sync_api import Page, expect

class AuthorizationPage():
    def __init__(self, page: Page) -> None:
        self.page = page
        self.username = page.locator("[data-test=\"username\"]")
        self.password = page.locator("[data-test=\"password\"]")
        self.button_to_login = page.locator("[data-test=\"login-button\"]")
    
    def login(self):
        self.page.goto('https://www.saucedemo.com/')
        self.username.fill('standard_user')
        self.password.fill('secret_sauce')
        self.button_to_login.click()
        expect(self.page.locator("[data-test=\"title\"]")).to_have_text('Products')