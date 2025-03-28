import re
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.product_list_page import ProductListPage
from pages.product_details_page import ProductDetailsPage
from pages.cart_page import CartPage

# Test adding a product to the shopping cart from the product details page.
def test_add_product_to_cart(page: Page,
                                      login_set_up,
                                      login_page: LoginPage,
                                      product_list_page: ProductListPage,
                                      product_details_page: ProductDetailsPage,
                                      cart_page: CartPage):

    product_list_page.click_product_link('Product 1')
    product_details_page.click_add_to_cart()
    expect(page).to_have_title(re.compile("Product Listing"))

    product_list_page.click_product_link('Product 2')
    product_details_page.click_add_to_cart()
    expect(page).to_have_title(re.compile("Product Listing"))

    product_list_page.click_view_cart()
    cart_page.cart_item_contains(['Product 1 - This is product 1. - Quantity: 1', 'Product 2 - This is product 2. - Quantity: 1'])
    expect(page).to_have_title(re.compile("View Cart"))
    expect(cart_page.get_cart_page_header()).to_contain_text("Cart")

    