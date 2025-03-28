import pytest
from pathlib import Path
from slugify import slugify
import datetime
import os
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.product_list_page import ProductListPage
from pages.product_details_page import ProductDetailsPage
from pages.cart_page import CartPage

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)

@pytest.fixture
def  product_list_page(page: Page) -> ProductListPage:
    return ProductListPage(page)

@pytest.fixture
def  product_details_page(page: Page) -> ProductDetailsPage:
    return ProductDetailsPage(page)

@pytest.fixture
def  cart_page(page: Page) -> CartPage:
    return CartPage(page)

@pytest.fixture()
def login_set_up(login_page: LoginPage):
    # Load environment variables from .env
    try:
        PASSWORD = os.environ['PASSWORD']
    except KeyError:
        import config.secret_config
        PASSWORD = config.secret_config.PASSWORD
    login_page.load()
    login_page.login('testuser', PASSWORD)

# # Hook to capture screenshot on test failure and attach screenshot to the file
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    screen_file = ''
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        xfail = hasattr(report, "wasxfail")
        if report.failed or xfail and "page" in item.funcargs:
            page = item.funcargs["page"]
            # Define the screenshot directory at the root of your project
            screenshot_dir = Path("reports/screenshots")  # Root-level folder for screenshots
            screenshot_dir.mkdir(exist_ok=True)

            # Generate the full path to the screenshot
            screenshot_path = screenshot_dir / f"{slugify(item.nodeid)}.png"
            page.screenshot(path=str(screenshot_path))

            # Add relative path to the HTML report
            screenshot_dir = Path("screenshots")
            rel_screenshot_path = os.path.relpath(screenshot_dir / f"{slugify(item.nodeid)}.png", Path("reports").parent)
            extra.append(pytest_html.extras.image(rel_screenshot_path))
        report.extras = extra