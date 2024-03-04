
def test_sportshop_e2e(desktop_sportshop):
    desktop_sportshop.open_url("https://sportshop.com.ua/")
    desktop_sportshop.switch_language_rus_ua()
    desktop_sportshop.autorithation()
    desktop_sportshop.search_product()
    desktop_sportshop.filtr_whey_protein()
    desktop_sportshop.sort_by_high_rating()
    desktop_sportshop.purchase_selected_product()
    desktop_sportshop.purchase_order()
    desktop_sportshop.delete_purchase()
    desktop_sportshop.feedback()
    desktop_sportshop.exit_account()
