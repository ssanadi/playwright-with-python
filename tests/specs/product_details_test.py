import re
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.product_list_page import ProductListPage
from pages.product_details_page import ProductDetailsPage

# Implement a test to verify that clicking on a product in the listing page navigates to the correct product details page.
def test_product_details(page: Page,
                         login_set_up,
                         product_list_page: ProductListPage,
                         product_details_page: ProductDetailsPage):

    # page.pause()
    product_list_page.click_product_link('Product 2')
    expect(page).to_have_title(re.compile("Product Details"))
    expect(product_details_page.product_details_page_header).to_contain_text("Product 2")
    expect(product_details_page.product_description).to_contain_text("This is product 2")
    expect(product_details_page.add_to_cart_link).to_be_visible()
    expect(product_details_page.view_cart_link).to_be_visible()
    