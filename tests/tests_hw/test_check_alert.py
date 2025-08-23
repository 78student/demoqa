import time

from pages.alerts import Alerts


def test_timer_alert_button(browser):
    alert_page = Alerts(browser)
    alert_page.visit()

    assert alert_page.btn_timer_alert.exist()
    alert_page.btn_timer_alert.click()
    time.sleep(7)

    assert alert_page.alert()