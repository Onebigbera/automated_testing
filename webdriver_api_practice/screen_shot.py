# -*-coding:utf-8 -*-
# File :screen_shot.py
# Author:George
# Date : 2019/10/11
# motto: Someone always give up while someone always try!
"""
    screen shot in web page
"""
from automated_testing.webdriver_api_practice.getDriver import get_driver
import time
import os


def get_screen_shot():
    """

    :return:
    """
    picture_directory = r'F:\Testing_Development\UnittestProjects\automated_testing\automated_testing\webdriver_api_practice\screen_shot'
    url = "https://www.runoob.com/python/python-tutorial.html"
    driver = get_driver()
    driver.get(url)
    time.sleep(3)
    try:
        if not os.path.exists(picture_directory):
            os.makedirs(picture_directory)
            print("make directory successfully")
        else:
            print("directory exists")
    except BaseException as e:
        print(e)
    # stringify the local time stamp
    time_now = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))
    try:
        # method 1
        picture_status = driver.get_screenshot_as_file(picture_directory + '\\' + time_now + '.png')
        print(picture_status)
    except BaseException as e:
        print(e)
    time.sleep(2)
    driver.close()


def save_screen_shot():
    """

    :return:
    """
    picture_directory = r'F:\Testing_Development\UnittestProjects\automated_testing\automated_testing\webdriver_api_practice\screen_shot'
    url = "https://www.runoob.com/python/python-tutorial.html"
    driver = get_driver()
    driver.get(url)
    time.sleep(3)
    try:
        if not os.path.exists(picture_directory):
            os.makedirs(picture_directory)
            print("make directory successfully")
        else:
            print("directory exists")
    except BaseException as e:
        print(e)
    # stringify the local time stamp
    time_now = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))
    try:
        # method 2
        picture_status = driver.save_screenshot(picture_directory + '\\' + time_now + '.png')
        print(picture_status)
    except BaseException as e:
        print(e)
    time.sleep(2)
    driver.close()
    pass


if __name__ == "__main__":
    get_screen_shot()
    # save_screen_shot()