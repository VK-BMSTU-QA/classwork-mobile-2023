import allure

from ui.locators.locators_mw import MainPagePageMWLocators
from ui.locators.locators_web import MainPageLocators
from ui.pages.base_page import BasePage


class MainPage(BasePage):
    locators = MainPageLocators()

    @allure.step("Нажимаем на кнопку поиска")
    def click_on_search_button(self):
        pass

    def open_menu_button(self):
        pass

    def open_watchlist(self):
        pass


class MainPageMW(MainPage):
    locators = MainPagePageMWLocators()

    @allure.step("Нажимаем на кнопку поиска")
    def click_on_search_button(self):
        self.click(self.locators.SEARCH_ICON)

    @allure.step("Нажимаем на кнопку открытия меню (mobile)")
    def open_menu_button(self):
        self.click(self.locators.MAIN_MENU)

    @allure.step("Нажимаем на кнопку открытия меню (mobile)")
    def open_watchlist(self):
        self.click(self.locators.WATCH_LIST)

