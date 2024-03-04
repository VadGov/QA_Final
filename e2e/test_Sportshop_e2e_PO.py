
def test_sportshop_e2e(desktop_sportshop):
    desktop_sportshop.open_url("https://sportshop.com.ua/")
    desktop_sportshop.change_lang_from_ua_on_rus_and_back()
    desktop_sportshop.autorithation()
    desktop_sportshop.search_product()
    desktop_sportshop.choice_whey_protein_in_filtr()
    desktop_sportshop.sort_by_high_rating()
    desktop_sportshop.purchase_selected_product()
    desktop_sportshop.purchase_order()
    desktop_sportshop.delete_purchase()
    desktop_sportshop.feedback()
    desktop_sportshop.exit_account()
