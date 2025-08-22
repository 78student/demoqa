import time

from pages.webtables import Webtables

def test_webtables_submit_empty(browser):
    web_table = Webtables(browser)
    web_table.visit()
    assert web_table.click_add()
    assert not web_table.submit_dialog()
    assert web_table.close_dialog()

def test_webtables_add_new_data(browser):
    web_table = Webtables(browser)
    web_table.visit()
    assert web_table.click_add()
    time.sleep(0.5)
    rows_count_before = len(web_table.get_rows())
    web_table.fill_dialog(
                first_name = 'Ivan',
                last_name = 'Ivanov',
                email = 'z@bn.ru',
                age = '30',
                salary = '1000',
                department = 'Security')
    assert web_table.submit_dialog()
    time.sleep(2)
    rows = web_table.get_rows()
    assert rows_count_before + 1 == len(rows)
    new_row = next((row for row in rows if row.department == 'Security'), None)
    assert not new_row is None
    assert new_row.first_name == 'Ivan' \
            and new_row.last_name == 'Ivanov' \
            and new_row.age == '30' \
            and new_row.email == 'z@bn.ru' \
            and new_row.salary == '1000'

def test_webtables_edit_existing_row(browser):
    web_table = Webtables(browser)
    web_table.visit()
    time.sleep(2)
    rows = web_table.get_rows()
    assert len(rows) > 0
    row = rows[0]
    assert row.click_edit()
    time.sleep(2)
    assert web_table.dialog_first_name.exist()
    assert row.first_name == web_table.dialog_first_name.get_dom_attribute('value') \
            and row.last_name == web_table.dialog_last_name.get_dom_attribute('value') \
            and row.age == web_table.dialog_age.get_dom_attribute('value') \
            and row.email == web_table.dialog_email.get_dom_attribute('value') \
            and row.salary == web_table.dialog_salary.get_dom_attribute('value')
    web_table.dialog_first_name.clear()
    web_table.dialog_first_name.send_keys('Testo')
    time.sleep(1)
    assert web_table.submit_dialog()
    time.sleep(2)
    rows = web_table.get_rows()
    assert len(rows) > 0
    row = next((row for row in rows if row.first_name == 'Testo'), None)
    assert not row is None

def test_webtables_delete_row(browser):
    web_table = Webtables(browser)
    web_table.visit()
    time.sleep(2)
    rows = web_table.get_rows()
    rows_count_before = len(rows)
    assert rows_count_before > 0
    deleted_name = rows[0].first_name
    assert rows[0].click_delete()
    time.sleep(2)
    rows = web_table.get_rows()
    assert rows_count_before - 1 == len(rows)
    row = next((row for row in rows if row.first_name == deleted_name), None)
    assert row is None