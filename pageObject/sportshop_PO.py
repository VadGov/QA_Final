from playwright.sync_api import Playwright


class SportShop:
    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

    def open_url(self, url: str):
        self.page.goto(url)

    def switch_language_rus_ua(self):
        self.page.get_by_role("button", name="Українська").click()
        self.page.get_by_text("Русский").click()
        # self.expect(page.get_by_text("СПОРТИВНОЕ ПИТАНИЕ")).to_be_visible()
        self.page.get_by_role("button", name="Русский").click()
        self.page.get_by_text("Українська").click()
        # self.expect(page.get_by_text("СПОРТИВНЕ ХАРЧУВАННЯ")).to_be_visible()

    def autorithation(self):
        self.page.get_by_role("button", name="Мій аккаунт").click()
        self.page.get_by_text("Авторизація / Реєстрація").click()
        self.page.get_by_placeholder("Електронна пошта").fill("dog71438@gmail.com")
        self.page.get_by_placeholder("Пароль").fill("v123456789d")
        self.page.get_by_role("button", name="Увійти").click()

    def search_product(self):
        self.page.locator("(//input[@placeholder='Що будемо шукати'])[1]").fill("mutant")
        self.page.locator(
            "div[class='col-hidden col-md-visible col-xl-4 pull-xl-3'] button[class='search__btn']").click()

    def filtr_whey_protein(self):
        self.page.locator("(//div[@class='jq-selectbox__select-text'])[1]").click()
        self.page.locator("li:nth-child(60)").click()
        self.page.get_by_role("button", name="Пошук").click()

    def sort_by_high_rating(self):
        self.page.get_by_role("button", name="Сортування: За замовчуванням").click()
        self.page.locator("div[class='options options--desktop'] li:nth-child(6)").click()

    def purchase_selected_product(self):
        self.page.locator("(//img[@alt='Mutant Whey Protein 2270 g'])[1]").click()
        self.page.locator("//button[@id='button-cart']").click()

    def purchase_order(self):
        self.page.locator("a[class='btn btn--blue']").click()

    def delete_purchase(self):
        self.page.locator(".cart__btn.js-toggle-btn").click()
        self.page.locator("//button[@title='Видалити']//*[name()='svg']").click()
        self.page.locator('[class="cart__back js-toggle-close"]').click()

    def feedback(self):
        self.page.locator("//a[@class='nav__link'][contains(text(),'Контакти')]").click()
        self.page.locator('[class="link link--dashed"]').click()
        self.page.locator("div[id='contact-form'] button[class='popup__close']").click()

    def exit_account(self):
        self.page.locator('[class="acc__btn js-toggle-btn"]').click()
        self.page.get_by_text("Вихід").click()

    def close(self):
        self.page.close()
        self.context.close()
        self.browser.close()
