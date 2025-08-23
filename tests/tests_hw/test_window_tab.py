import time

from selenium.webdriver.common.by import By


def test_link_home(browser):
    browser.get('https://demoqa.com/links')
    home_link = browser.find_element(By.ID,'simpleLink')
    assert home_link.text == 'Home'
    assert home_link.get_dom_attribute('href') == 'https://demoqa.com'
    window_handles_count_before = len(browser.window_handles)
    home_link.click()
    time.sleep(2)
    assert len(browser.window_handles) == window_handles_count_before + 1
