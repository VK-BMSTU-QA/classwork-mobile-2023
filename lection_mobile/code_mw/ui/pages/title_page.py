import allure

from ui.locators.locators_mw import TitlePagePageMWLocators
from ui.locators.locators_web import TitlePageLocators
from ui.pages.base_page import BasePage


class TitlePage(BasePage):
    locators = TitlePageLocators()

    def add_to_bookmark(self):
        pass


class TitlePageMW(TitlePage):
    locators = TitlePagePageMWLocators()

    @allure.step("Добавляем статью в избранное")
    def add_to_bookmark(self):
        self.click(self.locators.STAR_BUTTON)
