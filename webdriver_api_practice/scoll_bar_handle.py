# -*-coding:utf-8 -*-
# File :scoll_bar_handle.py
# Author:George
# Date : 2019/10/11
# motto: Someone always give up while someone always try!
"""
    scroll bar control
    us js action to control web page,by using js event to control page scroll, to analogy the SQL, we can also to use focus method
"""
from automated_testing.webdriver_api_practice.getDriver import get_driver
from time import sleep


def scroll_bar_controller():
    """
    use js to handle the scroll bar
    :return:
    """
    driver = get_driver()
    url = r'https://www.51zxw.net/'
    driver.get(url)
    sleep(2)

    # to drag the scroll bar to bottle
    js = "var action=document.documentElement.scrollTop=10000"
    driver.execute_script(js)

    sleep(3)
    js = "var action=document.documentElement.scrollTop=0"
    driver.execute_script(js)
    sleep(2)

    driver.close()


if __name__ == "__main__":
    scroll_bar_controller()

