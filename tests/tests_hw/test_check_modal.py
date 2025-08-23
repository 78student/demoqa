import pytest
import time

from selenium.common import WebDriverException

from pages.modal_dialogs import ModalDialogs

def test_modals(browser):
    try:
        modal_page = ModalDialogs(browser)
        modal_page.visit()
    except WebDriverException as ex:
        pytest.skip(f"URL unavailable {ex}")

    assert modal_page.btn_show_small.exist()
    modal_page.btn_show_small.click()
    time.sleep(1)
    assert modal_page.modal_dialog.exist()
    assert not modal_page.btn_close_large.exist()
    assert modal_page.btn_close_small.exist()
    modal_page.btn_close_small.click()
    time.sleep(1)
    assert not modal_page.modal_dialog.exist()

    assert modal_page.btn_show_large.exist()
    modal_page.btn_show_large.click()
    time.sleep(1)
    assert modal_page.modal_dialog.exist()
    assert modal_page.btn_close_large.exist()
    assert not modal_page.btn_close_small.exist()
    modal_page.btn_close_large.click()
    time.sleep(1)
    assert not modal_page.modal_dialog.exist()
