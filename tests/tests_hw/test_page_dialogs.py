import time

from pages.demoqa import DemoQa
from pages.modal_dialogs import ModalDialogs


def test_modal_elements(browser):
    modal_dialogs = ModalDialogs(browser)

    modal_dialogs.visit()

    assert modal_dialogs.menu_list.check_count_elements(count=5)

def test_navigation_modal(browser):
    navigation_modal = ModalDialogs(browser)

    navigation_modal.visit()
    navigation_modal.refresh()
    time.sleep(2)
    navigation_modal.icon.click()
    time.sleep(2)
    browser.back()
    time.sleep(2)
    browser.set_window_size(900, 400)
    time.sleep(2)
    browser.forward()
    time.sleep(2)
    demo_qa = DemoQa(browser)
    assert demo_qa.equal_url()
    assert demo_qa.equal_title()
    browser.set_window_size(1000, 1000)





