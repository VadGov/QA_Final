def test_Sportshop_e2e(desktop_sportshop):
    desktop_sportshop.open_url("https://sportshop.com.ua/")
    desktop_sportshop.localisation()
    desktop_sportshop.autorithation()
    desktop_sportshop.search()
    desktop_sportshop.sort()
    desktop_sportshop.filtr()
    desktop_sportshop.purchase_selection()
    desktop_sportshop.offer_purchese()
    desktop_sportshop.purchase_order()
    desktop_sportshop.feedback()
    desktop_sportshop.exit_acc()





