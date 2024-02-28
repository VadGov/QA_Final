from playwright.sync_api import Playwright


class SportShop:
    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()


    def close(self):
        self.page.close()
        self.context.close()
        self.browser.close()