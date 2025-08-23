from components.components import WebElement
from pages.base_page import BasePage


class ModalDialogs(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.ru/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.menu_list = WebElement(driver, '#app > div > div > div > div:nth-child(1) > div > div > div:nth-child(3) > div > ul > li')
        self.icon = WebElement(driver, '#app > header > a')
        self.btn_close_small = WebElement(driver, '#closeSmallModal')
        self.btn_close_large = WebElement(driver, '#closeLargeModal')
        self.btn_show_small = WebElement(driver, '#showSmallModal')
        self.btn_show_large = WebElement(driver, '#showLargeModal')
        self.modal_dialog = WebElement(driver, 'div.modal.show')

    def refresh(self, driver=None):
        self.driver.refresh()


