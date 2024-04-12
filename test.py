from playwright.sync_api import sync_playwright, Page
import pytest

# инициализация браузера на движке chromium
def initialize(p):
    browser = p.chromium.launch()
    page = browser.new_page()
    return browser, page


def test_case_1(page: Page):
    # https://www.avito.ru/web/1/charity/ecoImpact/init"
    # перехват микробэкенда, возвращающего данные
    page.route("**/web/1/charity/ecoImpact/init", lambda route: route.fulfill(path="jsons_test_cases/test_case_1.json"))
    # переход на тестируемую страницу
    page.goto('https://www.avito.ru/avito-care/eco-impact')
    # поиск счетчика по тексту в блоке
    page.get_by_text("Ваш экологический вклад").click()
    # скриншот данного участка
    page.screenshot(path="output/test_case_1.png")


def test_case_2(page: Page):
    # https://www.avito.ru/web/1/charity/ecoImpact/init"
    page.route("**/web/1/charity/ecoImpact/init", lambda route: route.fulfill(path="jsons_test_cases/test_case_2.json"))
    page.goto('https://www.avito.ru/avito-care/eco-impact')
    page.get_by_text("Ваш экологический вклад").click()
    page.screenshot(path="output/test_case_2.png")


def test_case_3(page: Page):
    # https://www.avito.ru/web/1/charity/ecoImpact/init"
    page.route("**/web/1/charity/ecoImpact/init", lambda route: route.fulfill(path="jsons_test_cases/test_case_3.json"))
    page.goto('https://www.avito.ru/avito-care/eco-impact')
    page.get_by_text("Ваш экологический вклад").click()
    page.screenshot(path="output/test_case_3.png")


def test_case_4(page: Page):
    # https://www.avito.ru/web/1/charity/ecoImpact/init"
    page.route("**/web/1/charity/ecoImpact/init", lambda route: route.fulfill(path="jsons_test_cases/test_case_4.json"))
    page.goto('https://www.avito.ru/avito-care/eco-impact')
    page.get_by_text("Ваш экологический вклад").click()
    page.screenshot(path="output/test_case_4.png")


def test_case_5(page: Page):
    # https://www.avito.ru/web/1/charity/ecoImpact/init"
    page.route("**/web/1/charity/ecoImpact/init", lambda route: route.fulfill(path="jsons_test_cases/test_case_5.json"))
    page.goto('https://www.avito.ru/avito-care/eco-impact')
    page.get_by_text("Ваш экологический вклад").click()
    page.screenshot(path="output/test_case_5.png")


def test_case_6(page: Page):
    # https://www.avito.ru/web/1/charity/ecoImpact/init"
    page.route("**/web/1/charity/ecoImpact/init", lambda route: route.fulfill(path="jsons_test_cases/test_case_6.json"))
    page.goto('https://www.avito.ru/avito-care/eco-impact')
    page.get_by_text("Ваш экологический вклад").click()
    page.screenshot(path="output/test_case_6.png")


def test_case_7(page: Page):
    # https://www.avito.ru/web/1/charity/ecoImpact/init"
    page.route("**/web/1/charity/ecoImpact/init", lambda route: route.fulfill(path="jsons_test_cases/test_case_7.json"))
    page.goto('https://www.avito.ru/avito-care/eco-impact')
    page.get_by_text("Ваш экологический вклад").click()
    page.screenshot(path="output/test_case_7.png")
