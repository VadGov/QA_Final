from playwright.sync_api import Playwright, sync_playwright, expect


def test_e2e_begin(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://sportshop.com.ua/")

    # Локалізація
    page.get_by_role("button", name="Українська").click()
    page.get_by_text("Русский").click()
    expect(page.get_by_text("СПОРТИВНОЕ ПИТАНИЕ")).to_be_visible()
    page.get_by_role("button", name="Русский").click()
    page.get_by_text("Українська").click()
    expect(page.get_by_text("СПОРТИВНЕ ХАРЧУВАННЯ")).to_be_visible()

    # Авторизація
    page.get_by_role("button", name="Мій аккаунт").click()
    page.get_by_text("Авторизація / Реєстрація").click()
    page.get_by_placeholder("Електронна пошта").fill("vadvadonik@gmail.com")
    page.get_by_placeholder("Пароль").fill("175935")
    page.get_by_role("button", name="Увійти").click()

    # пошук
    page.locator("(//input[@placeholder='Що будемо шукати'])[1]").fill("mutant")
    page.locator("div[class='col-hidden col-md-visible col-xl-4 pull-xl-3'] button[class='search__btn']").click()

    # фильтр по Сироватковий протїн
    page.locator("(//div[@class='jq-selectbox__select-text'])[1]").click()
    page.locator("li:nth-child(60)").click()
    page.get_by_role("button", name="Пошук").click()

    # сортировка
    page.get_by_role("button", name="Сортування: За замовчуванням").click()
    page.locator("div[class='options options--desktop'] li:nth-child(6)").click()

    # клик по карточке
    page.locator("(//img[@alt='Mutant Whey Protein 2270 g'])[1]").click()
    page.locator("//button[@id='button-cart']").click()

    # замовити
    page.locator("a[class='btn btn--blue']").click()

    # зворотній зв'язок
    page.locator("//a[@class='nav__link'][contains(text(),'Контакти')]").click()
    page.locator('[class="link link--dashed"]').click()
    page.locator("div[id='contact-form'] button[class='popup__close']").click()

    # Вихід з ос каб
    page.locator('[class="acc__btn js-toggle-btn"]').click()
    page.get_by_text("Вихід").click()

    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_e2e_begin(playwright)
