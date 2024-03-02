
def test_sportshop_e2e(desktop_sportshop):
    desktop_sportshop.open_url("https://sportshop.com.ua/")
    desktop_sportshop.localisation()
    desktop_sportshop.autorithation()
    desktop_sportshop.search()
    desktop_sportshop.filtr()
    desktop_sportshop.sort()
    desktop_sportshop.purchase_selection()
    desktop_sportshop.purchase_order()
    desktop_sportshop.delete_purchase()
    desktop_sportshop.feedback()
    desktop_sportshop.exit_acc()
