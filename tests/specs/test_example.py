import re
import pytest
from playwright.sync_api import Page, expect

@pytest.mark.skip
def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright_failed"))