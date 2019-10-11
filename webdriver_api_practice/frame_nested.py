# -*-coding:utf-8 -*-
# File :frame.py
# Author:George
# Date : 2019/10/10
# motto: Someone always give up while someone always try!
"""
    frame nested web page we need to know the HTML code of this structure
"""
from automated_testing.webdriver_api_practice.getDriver import get_driver
from time import sleep


def frame_nested_demo():
    """

    :return:
    """
    # url = r"http://localhost:63342/automated_testing/automated_testing/webdriver_api_practice/frame_demo.html?_ijt=uqnkn02h3irc5mljmqut1s5k38"
    url = r'F:\Testing_Development\UnittestProjects\automated_testing\automated_testing\webdriver_api_practice\frame_demo.html'
    driver = get_driver()
    driver.get(url)

    # use iframe id to switch
    # driver.switch_to_frame("search")
    driver.switch_to.frame("search")

    # operation in iframe
    driver.find_element_by_css_selector("#query").send_keys("Python")
    sleep(2)
    driver.find_element_by_css_selector("#stb")
    sleep(3)
    driver.close()


if __name__ == "__main__":
    frame_nested_demo()
