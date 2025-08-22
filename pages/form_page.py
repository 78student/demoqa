import time

from selenium.webdriver.common.by import By

from components.components import WebElement
from pages.base_page import BasePage


class FormPage(BasePage):


    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/automation-practice-form'
        super().__init__(driver, self.base_url)

        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.user_email = WebElement(driver, '#userEmail')
        self.gender_radio_1 = WebElement(driver, '#gender-radio-1')
        self.user_number = WebElement(driver, '#userNumber')
        self.btn_submit = WebElement(driver, '#submit')
        self.modal_dialog = WebElement(driver, 'body > div.fade.modal.show > div > div')
        self.btn_close_modal = WebElement(driver, '#closeLargeModal')
        self.hobbies = WebElement(driver, '#hobbies-checkbox-1')
        self.current_adress = WebElement(driver, '#currentAddress')

    def select_state(self, index: int):
        try:
            WebElement(self.driver, '#state > div > div:nth-of-type(2)').click_forse()
            WebElement(self.driver, '#state > div:nth-of-type(2) > div > div:nth-child(' + str(index) + ')').click_forse()
            #state > div:nth-of-type(2) [class=css-26l3qy-menu] > div > dev#react-select-3-option-XXX
            return True
        except:
            return False

    def get_state_text(self):
        return WebElement(self.driver, '#state > div > div:nth-child(1) > div').get_text()

