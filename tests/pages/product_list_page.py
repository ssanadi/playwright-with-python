from playwright.sync_api import Page
from typing import List

class ProductListPage:

    URL = '/product_listing'

    def __init__(self, page: Page) -> None:
        self.page = page
        self.product_list_page_header = page.locator('[data-testid="products-list-page-header"]')
        self.products = page.locator('//ul[@data-testid="product-list"]//child::a[contains(@href, "product_details")]')
        self.view_cart_link = page.locator('[data-testid="view-cart-link"]')

    def load(self) -> None:
        self.page.goto(self.URL)

    def get_all_products(self) -> List[str]:
        self.products.first.wait_for()
        return self.products.all_text_contents()

    def product_title_link_contains(self, productName: List[str]) -> bool:
        titles = self.get_all_products()
        return (titles.sort() == productName.sort())

    def click_product_link(self, productName: str):
        self.products.first.wait_for()
        items = self.products
        count = items.count()
        for i in range(count):
            if (items.nth(i).text_content() == productName):
                items.nth(i).click()
                break

    def click_view_cart(self):
        self.view_cart_link.click()
            

    def get_product_listing_page_header(self):
        return self.product_list_page_header
    
