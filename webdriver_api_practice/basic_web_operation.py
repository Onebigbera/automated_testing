# -*-coding:utf-8 -*-
# File :basic_web_operation.py
# Author:George
# Date : 2019/10/10
# motto: Someone always give up while someone always try!
"""
    basic web operation
"""
from automated_testing.webdriver_api_practice.getDriver import get_driver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.keys import Keys


def mouse_action():
    """
    common mouse action
    :return:
    """
    url = r'https://www.baidu.com'
    driver = get_driver()
    driver.get(url)
    # maximize the windows
    driver.maximize_window()
    # get input element
    element = driver.find_element_by_css_selector('#kw')
    element.send_keys("Python")
    sleep(3)
    # double click the input
    ActionChains(driver).double_click(element).perform()
    sleep(2)
    ActionChains(driver).context_click(element).perform()
    # click
    ActionChains(driver).click(element).perform()

    element.click()
    setting = driver.find_element_by_css_selector('.pf')
    ActionChains(driver).move_to_element(setting).perform()
    sleep(3)
    ActionChains(driver).reset_actions()
    sleep(4)
    driver.close()


def keyboard_action():
    """
    common keyboard action
    :return:
    """
    url =r"https://www.baidu.com"
    driver = get_driver()
    driver.get(url)
    driver.find_element_by_css_selector("#kw").send_keys("Python")
    sleep(2)
    # simulate keyboard action CTRL + A
    driver.find_element_by_css_selector("#kw").send_keys(Keys.CONTROL, 'a')

    driver.find_element_by_css_selector("#kw").send_keys(Keys.CONTROL, 'c')

    url = r'https://www.sogou.com/'
    driver.get(url)
    driver.find_element_by_css_selector(".sec-input").send_keys(Keys.CONTROL, 'v')
    sleep(3)
    driver.find_element_by_css_selector("#stb").click()
    sleep(3)
    driver.close()


if __name__ == "__main__":
    # mouse_action()
    keyboard_action()
