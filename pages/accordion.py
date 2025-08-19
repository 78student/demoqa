from pages.base_page import BasePage
from components.components import WebElement

class Accordion(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)
        self.section_content = WebElement(driver, "#section1Content > p")
        self.section_heading = WebElement(driver, "#section1Heading")
        self.section_content_child1 = WebElement(driver, "#section2Content > p:nth-child(1)")
        self.section_content_child2 = WebElement(driver, "#section2Content > p:nth-child(2)")
        self.section3_content = WebElement(driver, "#section3Content > p")