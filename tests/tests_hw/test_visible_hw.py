import time

from components.components import WebElement
from pages.demoqa import DemoQa
from pages.accordion import Accordion

def test_visible_accordion(browser):
    accordion = Accordion(browser)
    accordion.visit()
    assert  accordion.section_content.visible()
    accordion.section_heading.click()
    time.sleep(2)
    assert  not accordion.section_content.visible()

def test_visible_accordion_default(browser):
    accordion = Accordion(browser)
    accordion.visit()
    assert not accordion.section_content_child1.visible()
    assert not accordion.section_content_child2.visible()
    assert not accordion.section3_content.visible()



