import time

import allure
import pytest
from web_tests.base import BaseCase


class TestWikipediaWeb(BaseCase):
    @pytest.mark.MWUI
    @pytest.mark.UI
    @allure.severity(allure.severity_level.NORMAL)
    @allure.epic("Awesome PyTest framework")
    @allure.title("Test login")
    @allure.description("Test for login")
    @allure.feature('Login tests')
    def test_login(self):
        self.login_page.login()

    @pytest.mark.skip_platform("web")
    def test_saving_two_articles(self):
        text = 'Parkway Drive'
        self.login_page.login()
        with allure.step("Нажимаем на кнопку Search и вводим значения в поле ввода"):
            self.main_page.click_on_search_button()
            self.search_page.send_text_to_search_field_and_click_to_element(text, "Australian metalcore band")
        with allure.step("Добавляем статью в закладки"):
            self.title_page.add_to_bookmark()




