import re
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.product_list_page import ProductListPage
from pages.product_details_page import ProductDetailsPage

# Verify that after login, the user can navigate to the product listing page.
def test_product_listing(page: Page,
                         login_set_up,
                         product_list_page: ProductListPage):
    
    expect(product_list_page.get_product_listing_page_header()).to_contain_text("Products")
    assert product_list_page.product_title_link_contains(['Product 1', 'Product 2'])
    