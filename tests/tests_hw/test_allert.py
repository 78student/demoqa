import  time

from pages.alerts import Alerts

def test_alert(browser):
    alert_page = Alerts(browser)

    alert_page.visit()
    assert not alert_page.alert()

    alert_page.btn_alert.click()
    time.sleep()
    assert alert_page.alert()

def test_alert_text(browser):
    alert_page =Alerts(browser)

    alert_page.visit()
    alert_page.btn_alert.click()
    assert alert_page.alert().text == 'You clicked a button'

    alert_page.alert().accept()
    assert not alert_page.alert()

