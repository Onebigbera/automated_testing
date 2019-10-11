# -*-coding:utf-8 -*-
# File :multi_windows_switch.py
# Author:George
# Date : 2019/10/10
# motto: Someone always give up while someone always try!
"""
    multi windows switch
"""
from automated_testing.webdriver_api_practice.getDriver import get_driver
from time import sleep


def multi_windows_switch():
    """

    :return:
    """
    url = r'https://www.51zxw.net/List.aspx?cid=615#!fenye=4'
    driver = get_driver()
    driver.get(url)
    # get current page handle
    handle_current = driver.current_window_handle

    driver.find_element_by_partial_link_text("4-27 文件").click()
    sleep(3)
    # switch to before page by handle
    driver.switch_to.window(handle_current)
    sleep(3)
    driver.find_element_by_xpath("//a[contains(text(),'4-25')]").click()
    sleep(2)
    driver.close()


if __name__ == "__main__":
    multi_windows_switch()