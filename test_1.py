import time
import yaml

from module import Site

with open("testdata.yaml", "r") as file:
    testdata = yaml.safe_load(file)

site = Site(testdata["address"])

def test_step_1(x_selector_1, x_selector_2, x_selector_3, btn_selector):
    input_1 = site.find_element("xpath", x_selector_1)
    input_1.send_keys("test")
    input_2 = site.find_element("xpath", x_selector_2)
    input_2.send_keys("test")
    btn = site.find_element("css", btn_selector)
    btn.click()
    err_label = site.find_element("xpath", x_selector_3)
    assert err_label.text == "401"

def test_step_2(x_selector_1, x_selector_2, btn_selector, result_log):
    input_1 = site.find_element("xpath", x_selector_1)
    input_1.send_keys(testdata["login"])
    input_2 = site.find_element("xpath", x_selector_2)
    input_2.send_keys(testdata["password"])
    btn = site.find_element("css", btn_selector)
    btn.click()
    result_label = site.find_element("xpath", result_log)
    assert result_label.text == "Blog"


def test_step_3(x_selector_1, x_selector_2, btn_selector, btn_create_post, new_post_text):
    input_1 = site.find_element("xpath", x_selector_1)
    input_1.send_keys(testdata["login"])
    input_2 = site.find_element("xpath", x_selector_2)
    input_2.send_keys(testdata["password"])
    btn = site.find_element("css", btn_selector)
    btn.click()
    btn_create_post = site.find_element("xpath", btn_create_post)
    btn_create_post.click()
    result_text = site.find_element("xpath", new_post_text)
    assert result_text.text == "Create Post"



def test_step_4(x_selector_1, x_selector_2, btn_selector, btn_create_post, selector_title, fill_title,
                selector_description, fill_description, fill_content, selector_content, btn_save_post, file_input,
                upload_img, result_log, revealed=None):
    input_1 = site.find_element("xpath", x_selector_1)
    input_1.send_keys(testdata["login"])
    input_2 = site.find_element("xpath", x_selector_2)
    input_2.send_keys(testdata["password"])
    btn = site.find_element("css", btn_selector)
    btn.click()
    btn_create_post = site.find_element("xpath", btn_create_post)
    btn_create_post.click()
    selector_title = site.find_element("xpath", selector_title)
    selector_title.send_keys(fill_title)
    selector_description = site.find_element("xpath", selector_description)
    selector_description.send_keys(fill_description)
    select_content = site.find_element("xpath", selector_content)
    select_content.send_keys(fill_content)
    file_input = site.find_element("xpath", file_input)
    file_input.send_keys(upload_img)
    time.sleep(2)
    btn_save_post = site.find_element("xpath", btn_save_post)
    btn_save_post.click()
    time.sleep(2)
    selector_home = site.find_element("xpath", """//*[@id="app"]/main/nav/a/span""")
    selector_home.click()
    result_label = site.find_element("xpath", result_log)
    assert result_label.text == 'Selenium'




# css_selector = "span.mdc-text-field__ripple"
# print(site.get_element_property("css", css_selector, "height"))
#
# xpath_selector = '//*[@id="login"]/div[3]/button/div'
# print(site.get_element_property("xpath", xpath_selector, "color"))