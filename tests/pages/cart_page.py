from playwright.sync_api import Page
from typing import List

class CartPage:

    URL = '/view_cart'

    def __init__(self, page: Page) -> None:
        self.page = page
        self.cart_page_header = page.locator('[data-testid="cart-page-header"]')
        self.cart_items = page.locator('//ul[@data-testid="product-list"]//child::li')
        self.product_list_link = page.locator('[data-testid="product-listing-link"]')
    
    def load(self) -> None:
        self.page.goto(self.URL)

    def get_all_products_text_in_cart(self) -> List[str]:
        self.cart_items.first.wait_for()
        return self.cart_items.all_text_contents()

    def cart_item_contains(self, items: List[str]) -> bool:
        items = self.get_all_products_text_in_cart()
        return (items.sort() == items.sort())            

    def get_cart_page_header(self):
        return self.cart_page_header

    def click_go_back_to_product_list_cart(self):
        self.product_list_link.click()

    
    
