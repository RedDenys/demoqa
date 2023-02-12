import time

from pages.tb_page import TextboxPage

def test_box_page(browser):
    tbox_page = TextboxPage(browser)
    tbox_page.visit()
    time.sleep(4)
    tbox_page.user_name.send_keys('Tamango')
    tbox_page.current_address.send_keys('Bolívar 1 C1066AAA CABA Argentina')
