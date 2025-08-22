import time

from components.components import WebElement

def test_text_box(browser):
    browser.get('https://demoqa.com/text-box')

    user_name = WebElement(browser, '#userName')
    user_name.send_keys('Name')
    current_address = WebElement(browser, 'textarea#currentAddress')
    current_address.send_keys('Address')


    submit = WebElement(browser, '#submit')
    submit.click()
    time.sleep(2)

    user_name_text = WebElement(browser, 'p#name')
    current_address_text = WebElement(browser, 'p#currentAddress')
    assert user_name_text.get_text() == 'Name:Name'
    assert current_address_text.get_text() == 'Current Address :Address'










