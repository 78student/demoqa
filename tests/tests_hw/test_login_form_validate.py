import time

from selenium.webdriver.common.by import By
from components.components import WebElement
from conftest import browser

def test_text_box(browser):
    browser.get('https://demoqa.com/automation-practice-form')

    first_name = WebElement(browser, '#firstName')
    last_name = WebElement(browser, '#lastName')
    email = WebElement(browser, '#userEmail')

    assert first_name.get_dom_attribute('placeholder') == 'First Name'
    assert last_name.get_dom_attribute('placeholder') == 'Last Name'
    assert email.get_dom_attribute('placeholder') == 'name@example.com'
    assert email.get_dom_attribute('pattern') == '^([a-zA-Z0-9_\\-\\.]+)@([a-zA-Z0-9_\\-\\.]+)\\.([a-zA-Z]{2,5})$'

    submit = WebElement(browser, '#submit')
    submit.click_forse()
    time.sleep(1)
    user_form = WebElement(browser, '#userForm.was-validated')
    assert user_form.exist()



