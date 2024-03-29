from playwright.sync_api import expect


# Перевірка зміни адреси доставки користувача
# def test_change_address_delivery(browser):
#     context = browser.new_context()
#     page = context.new_page()
#
#     page.goto("https://sportshop.com.ua/")
#     page.get_by_role("button", name="Мій аккаунт").click()
#     page.get_by_text("Авторизація / Реєстрація").click()
#     page.get_by_placeholder("Електронна пошта").fill("dog71438@gmail.com")
#     page.get_by_placeholder("Пароль").fill("v123456789d")
#     page.get_by_role("button", name="Увійти").click()
#     page.locator("//span[contains(text(),'Зміна адрес')]").click()
#     page.locator(".btn.btn--sm.btn--transparent").click()
#     page.locator("#address_city").fill("Полтава")
#     page.locator("#address_address_1").fill("Відділення №5 (до 30 кг): просп. Свободи (ран. 60-річчя Жовтня)")
#     page.locator("div[class='personal__action'] button[type='submit']").click()
#     element = page.get_by_text('Адресу змінено')
#     expect(element).to_be_visible()


# Перевірка зміни им'я та прізвища користувача
def test_change_name_and_surname(browser):
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://sportshop.com.ua/")
    page.get_by_role("button", name="Мій аккаунт").click()
    page.get_by_text("Авторизація / Реєстрація").click()
    page.get_by_placeholder("Електронна пошта").fill("dog71438@gmail.com")
    page.get_by_placeholder("Пароль").fill("v123456789d")
    page.get_by_role("button", name="Увійти").click()
    page.locator("//span[contains(text(),'Контактна інформація')]").click()
    page.locator("#edit_firstname").fill("ololo")
    page.locator("#edit_lastname").fill("Бімбімбамбам")
    page.locator('[class="button btn-primary button_oc btn"]').click()
    element = page.locator('[class="alert alert-success alert-dismissible fade show"]')
    expect(element).to_be_visible()

    context.close()



# Перевірка авторизації після вводу невалідних даних
def test_invalid_login(browser):
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://sportshop.com.ua/")
    page.get_by_role("button", name="Мій аккаунт").click()
    page.get_by_text("Авторизація / Реєстрація").click()
    page.get_by_placeholder("Електронна пошта").fill("іфвфв@adaad.сщь")
    page.get_by_placeholder("Пароль").fill("-1125")
    page.get_by_role("button", name="Увійти").click()
    result = page.get_by_text('Мій аккаунт')
    expect(result).to_be_visible()

    context.close()


# Перевірка функції пошука(header) без вводу даних (можливий баг)
def test_empty_search_header_(browser):
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://sportshop.com.ua/")
    page.locator("div[class='col-hidden col-md-visible col-xl-4 pull-xl-3'] button[class='search__btn']").click()
    result = page.locator(
        "div[class='col-hidden col-md-visible col-xl-4 pull-xl-3'] input[placeholder='Що будемо шукати']")

    if result:
        # результат не є порожнім
        print("Поле пошуку не є порожнім")
    else:
        #  результат порожній
        print("Поле пошуку є порожнім")

    context.close()
