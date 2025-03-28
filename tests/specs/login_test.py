import re
import pytest
import os
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.product_list_page import ProductListPage

# Load secret variables
try:
    PASSWORD = os.environ['PASSWORD']
except KeyError:
    import config.secret_config
    PASSWORD = config.secret_config.PASSWORD

# Verify that a user can log in with valid credentials.
def test_login_with_valid_credentials(page: Page,
                                      login_page: LoginPage,
                                      product_list_page: ProductListPage):
    # login_page = LoginPage(page)
    # product_list_page= ProductListPage(page)

    login_page.load()
    login_page.login('testuser', PASSWORD)

    # Verify that after login, the user can navigate to the product listing page.
    expect(product_list_page.get_product_listing_page_header()).to_contain_text("Products")
    expect(page).to_have_title(re.compile("Product Listing"))
    
#  Ensure the system correctly handles invalid login attempts.
@pytest.mark.parametrize("email, password", [('TESTUSER', 'PASSWORD123'),
                                              ('testuser', 'PASSWORD123'),
                                              ('TESTUSER', 'password123')])
def test_login_with_invalid_credentials(page: Page,
                                        login_page: LoginPage,
                                        email,
                                        password):
    # login_page = LoginPage(page)

    login_page.load()
    login_page.login(email, password)
    expect(login_page.invalid_login_message).to_contain_text("Invalid credentials. Please try again.")


#  Failed test scenario - Ensure screenshot is attached to HTML report
@pytest.mark.parametrize("email, password", [('TESTUSER', 'PASSWORD123'),
                                              ('testuser', 'PASSWORD123')])
@pytest.mark.skip
def test_login_with_invalid_credentials_screenshot_scenario(page: Page,
                                        login_page: LoginPage,
                                        product_list_page: ProductListPage,
                                        email,
                                        password):
    # login_page = LoginPage(page)

    login_page.load()
    login_page.login(email, password)
    expect(product_list_page.get_product_listing_page_header()).to_contain_text("Products")