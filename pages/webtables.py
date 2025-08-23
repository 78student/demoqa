import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from components.components import WebElement
from pages.base_page import BasePage


def get_element_text(root, location) -> str | None:
    try:
        text = root.find_element(By.CSS_SELECTOR, location).text
        return text
    except NoSuchElementException:
        return None


class Webtables(BasePage):
    # region table row
    class TableRow:
        def __init__(self, row_element):
            try:
                text = row_element.text
            except:
                text = None

            self.empty = text is None or len(str(text).strip()) == 0
            if self.empty:
                self.first_name = None
                self.last_name = None
                self.age = None
                self.email = None
                self.salary = None
                self.department = None
                self.edit = None
                self.delete = None
            else:
                self.first_name = get_element_text(row_element, 'div.rt-tr > div:nth-of-type(1)')
                self.last_name = get_element_text(row_element, 'div.rt-tr > div:nth-of-type(2)')
                self.age = get_element_text(row_element, 'div.rt-tr > div:nth-of-type(3)')
                self.email = get_element_text(row_element, 'div.rt-tr > div:nth-of-type(4)')
                self.salary = get_element_text(row_element, 'div.rt-tr > div:nth-of-type(5)')
                self.department = get_element_text(row_element, 'div.rt-tr > div:nth-of-type(6)')
                self.edit = row_element.find_element(By.CSS_SELECTOR, 'div.rt-tr div.action-buttons > span:nth-child(1)')
                self.delete = row_element.find_element(By.CSS_SELECTOR, 'div.rt-tr div.action-buttons > span:nth-child(2)')

        def click_edit(self):
            if self.edit is None:
                return False
            try:
                self.edit.click()
                return True
            except:
                return False

        def click_delete(self):
            if self.delete is None:
                return False
            try:
                self.delete.click()
                return True
            except:
                return False

    # endregion

    # region table header
    class TableHeader:
        def __init__(self, header_element):
            self.root = header_element

        def get_columns(self):
            return [item for item in self.root.find_elements(By.CSS_SELECTOR, 'div.rt-th')]

        def get_column(self, col_id: str|int):
            if col_id is str:
                return next((col for col in self.get_columns() if col.text == col_id), None)
            elif col_id is int:
                return self.get_columns()[col_id]
            return None
    # endregion

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.btn_add = WebElement(driver, '#addNewRecordButton')
        self.dialog = WebElement(driver, 'body > div.fade.modal.show')
        self.dialog_submit =WebElement(driver, '#submit')
        self.dialog_close = WebElement(driver, 'body > div.fade.modal.show > div > div > div.modal-header > button')
        self.dialog_form_validated = WebElement(driver, '#userForm.was-validated')
        self.dialog_first_name =WebElement(driver, '#firstName')
        self.dialog_last_name = WebElement(driver, '#lastName')
        self.dialog_email = WebElement(driver, '#userEmail')
        self.dialog_age = WebElement(driver, '#age')
        self.dialog_salary = WebElement(driver, '#salary')
        self.dialog_department = WebElement(driver, '#department')
        self.table_rows = WebElement(driver, 'div.rt-table > div.rt-tbody > div')
        self.table_header = WebElement(driver, 'div.ReactTable > div.rt-table > div.rt-thead.-header > div')

    def click_add(self):
        self.btn_add.click_forse()
        time.sleep(0.5)
        return self.dialog.exist()

    def close_dialog(self):
        if self.dialog_close.exist():
            self.dialog_close.click_forse()
            time.sleep(0.5)
            return not self.dialog.exist()
        return True

    def submit_dialog(self):
        if self.dialog_submit.exist():
            self.dialog_submit.click_forse()
            time.sleep(0.5)
            return not self.dialog.exist()
        return False

    def is_dialog_validated(self):
        return self.dialog_form_validated.exist()

    def fill_dialog(self, first_name = None, last_name = None, email = None, age = None, salary = None, department = None):
        if self.dialog_submit.exist():
            if not first_name is None:
                self.dialog_first_name.send_keys(first_name)
            if not last_name is None:
                self.dialog_last_name.send_keys(last_name)
            if not email is None:
                self.dialog_email.send_keys(email)
            if not age is None:
                self.dialog_age.send_keys(age)
            if not salary is None:
                self.dialog_salary.send_keys(salary)
            if not department is None:
                self.dialog_department.send_keys(department)

    def get_rows(self):
        rows = [self.TableRow(row) for row in self.table_rows.find_elements()]
        return [row for row in rows if not row.empty]

    def get_header(self):
        return self.TableHeader(self.table_header.find_element())