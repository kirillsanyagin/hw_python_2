import pytest


@pytest.fixture()
def x_selector_1():
    return """//*[@id="login"]/div[1]/label/input"""

@pytest.fixture()
def x_selector_2():
    return """//*[@id="login"]/div[2]/label/input"""


@pytest.fixture()
def x_selector_3():
    return """//*[@id="app"]/main/div/div/div[2]/h2"""

@pytest.fixture()
def btn_selector():
    return """button"""

@pytest.fixture()
def result_log():
    return """//*[@id="app"]/main/div/div[1]/h1"""

@pytest.fixture()
def btn_create_post():
    return """//*[@id="create-btn"]"""


@pytest.fixture()
def new_post_text():
    return """//*[@id="app"]/main/div/div/h1"""

@pytest.fixture()
def selector_title():
    return """//*[@id="create-item"]/div/div/div[1]/div/label/input"""
@pytest.fixture()
def fill_title():
    return "Selenium"

@pytest.fixture()
def selector_description():
    return """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""
@pytest.fixture()
def fill_description():
    return "Набор инструментов и библиотек с открытым исходным кодом"

@pytest.fixture()
def selector_content():
    return """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""
@pytest.fixture()
def fill_content():
    return ("Selenium — это набор инструментов и библиотек с открытым исходным кодом, "
            "которые автоматизируют тестирование веб-сайтов и веб-приложений.")

@pytest.fixture()
def file_input():
    return """//*[@id="create-item"]/div/div/div[6]/div/div/label/input"""
@pytest.fixture()
def upload_img():
    return "/Users/veles/PycharmProjects/lesson_2/Selenium_Logo-1.png"

@pytest.fixture()
def btn_save_post():
    return """//*[@id="create-item"]/div/div/div[7]/div/button"""