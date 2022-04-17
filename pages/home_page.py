from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from time import sleep


class HomePage(BasePage):

    ACCEPT_COOKIES_BTN = (By.XPATH, '//button[text()="Accept"]')
    INTRA_IN_CONT_BTN = (By.XPATH, '(//a[text()="Intra in cont"])[2]')
    SALUT_MSG = (By.XPATH, '//p/strong[contains(text(), "Salut")]')
    SEARCH_INPUT = (By.ID, 'searchboxTrigger')

    def navigate_to_home_page(self):
        self.driver.get('https://www.emag.ro/')

    def click_accept_cookies_btn(self):
        self.click_if_present(*self.ACCEPT_COOKIES_BTN)

    def search_after(self, query):
        self.wait_and_fill_elem(*self.SEARCH_INPUT, query)
        self.driver.find_element(*self.SEARCH_INPUT).send_keys(Keys.ENTER)
        sleep(1)

    def click_contul_meu_btn(self):
        self.wait_and_click_elem(*self.INTRA_IN_CONT_BTN)

    def verify_login_message(self, expected_msg):
        self.verify_text_on_elem(*self.SALUT_MSG, expected_msg)

    def verify_url_message(self):
        self.verify_page_url('https://www.emag.ro/')





