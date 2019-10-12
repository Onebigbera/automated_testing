# -*-coding:utf-8 -*-
# File :login_page.py
# Author:George
# Date : 2019/10/12
# motto: Someone always give up while someone always try!
from basepage import BasePage
from selenium.webdriver.common.by import By
import unittest
import logging.config

# get logging instance by file config  all config are in log.conf file
CON_LOG = 'log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()


class LoginPage(BasePage):
    url = "/"

    # locator  tuple and it will packaging in using of *args
    username_loc = (By.NAME, 'username')
    password_loc = (By.NAME, 'password')
    submit_loc = (By.NAME, 'Submit')

    def type_username(self, username):
        """use *(username_loc) can packaging the tuple"""
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self, password):
        """use *(password_loc) can packing the tuple"""
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)

    def submit_click(self):
        self.find_element(*self.submit_loc).click()


def test_login_action(driver, username, password):
    logging.info("====start test===")
    login_page = LoginPage(driver)
    logging.info("===get_driver===")

    login_page.type_username(username)
    logging.info("=== type username===")

    login_page.type_password(password)
    logging.info("===type password===")

    login_page.submit_click()
    logging.info("===finished===")









