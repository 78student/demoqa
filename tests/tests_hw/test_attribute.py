#import  time

from pages.text_box import  TextBox

def text_placeholder(browser):
    text_box_page = TextBox(browser)

    text_box_page.visit()
    assert text_box_page.name.get_dom_attribute('placeholder') == 'Full Name'