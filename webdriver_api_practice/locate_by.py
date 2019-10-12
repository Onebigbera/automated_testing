# -*-coding:utf-8 -*-
# File :locate_by.py
# Author:George
# Date : 2019/10/12
# motto: Someone always give up while someone always try!
"""
    BY locate method  easy to packaging and decoupling
"""
from time import sleep

from automated_testing.webdriver_api_practice.getDriver import get_driver
from selenium.webdriver.common.by import By


def locate_id_name():
    """
    locate by id or name
    :return:
    """
    url = r'https://www.baidu.com'
    driver = get_driver()
    driver.get(url)
    # driver.find_element_by_id("kw").send_keys("Python")
    driver.find_element(By.ID, 'kw').send_keys("Python")
    sleep(2)
    # driver.find_element_by_id("kw").clear()
    driver.find_element(By.ID, "kw").clear()
    sleep(2)
    # driver.find_element_by_name("wd").send_keys("Selenium")
    driver.find_element(By.NAME, "wd").send_keys("Selenium")
    sleep(3)
    # driver.find_element_by_id("su").click()
    driver.find_element(By.ID, "su").click()
    # driver.find_element(By.CLASS_NAME, class_name).click()
    driver.find_element(By.ID, "su").click()
    # driver.find_element(By.CSS_SELECTOR, css_selector).click()
    # driver.find_element(By.XPATH, xpath_selector).click()
    # driver.find_element(By.LINK_TEXT, link_text).click()
    # driver.find_element(By.PARTIAL_LINK_TEXT, partial_link_text).click()
    sleep(3)
    driver.close()


if __name__ == "__main__":
    locate_id_name()