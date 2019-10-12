# -*-coding:utf-8 -*-
# File :test_login.py
# Author:George
# Date : 2019/10/12
# motto: Someone always give up while someone always try!
from time import sleep

from login_action import *
import unittest
from automated_testing.webdriver_api_practice.getDriver import get_driver


if __name__ == "__main__":
    """
        We can also add login,and generate test report and send the report to relative manager
    """
    driver = get_driver()
    username = 'username'
    password = 'password'
    test_login_action(driver, username, password)
    sleep(3)
    driver.quit()