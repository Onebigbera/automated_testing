# -*-coding:utf-8 -*-
# File :test_51zxw.py
# Author:George
# Date : 2019/10/12
# motto: Someone always give up while someone always try!
"""
    to test simple unittest case of login baidu
"""
from time import sleep

from selenium.common.exceptions import NoSuchElementException

from automated_testing.webdriver_api_practice.getDriver import get_driver
import unittest


class WebTest(unittest.TestCase):

    def setUp(self):
        self.driver = get_driver()
        url = r'https://www.baidu.com'
        self.driver.implicitly_wait(5)
        self.driver.get(url)

    def testbaidu(self):
        """baidusearch"""
        driver = self.driver
        url = r"https://www.baidu.com"
        driver.get(url)
        # set driver wait 5 seconds for all the page elements
        driver.implicitly_wait(5)

        try:
            driver.find_element_by_css_selector("#kw").send_keys("Python")
            driver.find_element_by_css_selector("#su").click()
        except NoSuchElementException as e:
            print(e)
        finally:
            print("Process finished!")
        sleep(3)
        self.assertEqual(driver.title, 'Python_百度搜索')

    def tearDown(self):
        driver = self.driver
        driver.close()



