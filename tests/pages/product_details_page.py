from playwright.sync_api import Page
from typing import List

class ProductDetailsPage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.product_details_page_header = page.locator('[data-testid="product-details-page-header"]')
        self.product_description = page.locator('[data-testid="product-description-para"]')
        self.add_to_cart_link = page.locator('[data-testid="add-to-cart-link"]')
        self.view_cart_link = page.locator('[data-testid="view-cart-link"]')

    def get_all_products(self) -> List[str]:
        self.products.first.wait_for()
        return self.products.all_text_contents()

    def product_title_link_contains(self, productName: List[str]) -> bool:
        titles = self.get_all_products()
        return (titles.sort() == productName.sort())            

    def get_product_details_page_header(self):
        return self.product_details_page_header

    def get_product_description(self):
        return self.product_description

    def click_add_to_cart(self):
        self.add_to_cart_link.click()

    def click_view_cart(self):
        self.view_cart_link.click()

    
    
