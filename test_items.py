import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_check_bucket_button(browser):
    browser.get(link)
    bucket_button = browser.find_element_by_css_selector('.btn-add-to-basket')
    assert bucket_button, "Кнопки добавления в корзину нет на странице!"
