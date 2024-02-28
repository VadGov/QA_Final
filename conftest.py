from playwright.sync_api import  sync_playwright
from pytest import fixture
from pageObject.sportshop_PO import SportShop


@fixture()
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright




@fixture()
def desktop_Sportshop(get_playwright):
    desktop_Sportshop = Sportshop(get_playwright)
    yield desktop_Sportshop
    desktop_Sportshop.close()
