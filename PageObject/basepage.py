# -*-coding:utf-8 -*-
# File :page.py
# Author:George
# Date : 2019/10/12
# motto: Someone always give up while someone always try!

from automated_testing.webdriver_api_practice.getDriver import get_driver
from time import sleep


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://www.baidu.com'
        self.timeout = 10

    def _open(self, url):
        """
        the private method
        :param url: the detail url
        :return:
        """
        url_ = self.base_url + url
        print("Current url is {}".format(url_))
        self.driver.maximize_window()
        self.driver.get(url_)
        sleep(2)
        assert self.driver.current_url == url_, 'Did not load on {}'.format(url_)

    def open(self, url):
        """
        public method to invoke private method
        :return:
        """
        self._open(url)

    def find_element(self, *args):
        """
        find element  *args will packaging automated  just like (BY.ID, id)  return the element
        :param args:
        :return:
        """
        return self.driver.find_element(*args)



