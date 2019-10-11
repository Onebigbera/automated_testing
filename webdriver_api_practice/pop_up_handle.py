# -*-coding:utf-8 -*-
# File :pop_up_handle.py
# Author:George
# Date : 2019/10/11
# motto: Someone always give up while someone always try!
"""
    to deal with the pop up handle
"""
from automated_testing.webdriver_api_practice.getDriver import get_driver
from time import sleep


def pop_up_windows_handle():
    """

    :return:
    """
    url = r'https://www.baidu.com'
    driver = get_driver()
    driver.get(url)

    driver.find_element_by_link_text("设置").click()
    # todo : why this lose efficacy with name location
    # driver.find_element_by_name("tj_settingicon").click()
    sleep(2)
    # thought we can't find this element in web page content but we can still operate it with location
    driver.find_element_by_link_text("搜索设置").click()
    sleep(2)
    driver.find_element_by_link_text("保存设置").click()
    sleep(2)

    # initialize  a alert object
    alert = driver.switch_to.alert
    alert.accept()
    sleep(3)
    driver.close()


if __name__ == "__main__":
    pop_up_windows_handle()
