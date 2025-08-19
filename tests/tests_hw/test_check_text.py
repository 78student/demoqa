from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage


def test_check_icon(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    assert demo_qa_page.footer.get_text() == "© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED."

def test_check_elements_center_text(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    elements_page = demo_qa_page.click_elements()
    assert elements_page.equal_url()
    assert elements_page.center.get_text() == 'Please select an item from left to start practice.'

def test_page_elements(browser):
    el_page = ElementsPage(browser)
    el_page.visit()

    assert el_page.icon.exist()
    assert el_page.btn_sidebar_first.exist()
    assert el_page.btn_sidebar_first_textbox.exist()
