from playwright.sync_api import sync_playwright
from pytest import fixture

from pageObject.sportshop_PO import SportShop


@fixture()
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@fixture()
def desktop_sportshop(get_playwright):
    sportshop = SportShop(get_playwright)
    yield sportshop
    sportshop.close()
