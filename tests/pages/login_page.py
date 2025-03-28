from playwright.sync_api import Page

class LoginPage:

    URL = '/login'

    def __init__(self, page: Page) -> None:
        self.page = page
        self.username_input = page.locator('[data-testid="username-input"]')
        self.password_input = page.locator('[data-testid="password-input"]')
        self.login_button = page.locator('[data-testid="login-button"]')
        self.invalid_login_message = page.locator('//body')

    def load(self) -> None:
        self.page.goto(self.URL)

    def login(self, username: str, password: str) -> None:
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

