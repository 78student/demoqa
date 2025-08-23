import time

from pages.webtables import Webtables


def test_table_sorting(browser):
    web_tables = Webtables(browser)
    web_tables.visit()
    time.sleep(1)
    header = web_tables.get_header()
    for col in header.get_columns():
        clazz = col.get_dom_attribute('class')
        # нет сортировки
        assert len([cls for cls in str(clazz).split(' ') if cls.startswith('-sort')]) == 0
        col.click()
        time.sleep(0.1)
        clazz = col.get_dom_attribute('class')
        # сортировка по возрастанию
        assert '-sort-asc' in str(clazz).split(' ')
        col.click()
        time.sleep(0.1)
        clazz = col.get_dom_attribute('class')
        # сортировка по убыванию
        assert '-sort-desc' in str(clazz).split(' ')


