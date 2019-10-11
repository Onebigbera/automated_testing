# -*-coding:utf-8 -*-
# File :selenium_apis.py
# Author:George
# Date : 2019/10/10
# motto: Someone always give up while someone always try!
"""
    show how selenium invoke webdriver to realize automated
"""
from automated_testing.webdriver_api_practice.getDriver import get_driver
from time import sleep
from selenium.webdriver.support.ui import Select


def basic_operation():
    """
    open、quit
    :return:
    """
    url = r'https://www.51zxw.net/Show.aspx?cid=615&id=60545'
    driver = get_driver()
    driver.get(url)
    sleep(3)
    print("current website title is:{}".format(driver.title))
    print("current website url is:{}".format(driver.current_url))
    driver.close()


def locate_id_name():
    """
    locate by id or name
    :return:
    """
    url = r'https://www.baidu.com'
    driver = get_driver()
    driver.get(url)
    driver.find_element_by_id("kw").send_keys("Python")
    sleep(2)
    driver.find_element_by_id("kw").clear()
    sleep(2)
    driver.find_element_by_name("wd").send_keys("Selenium")
    sleep(3)
    driver.find_element_by_id("su").click()
    sleep(3)
    driver.close()


def locate_tag_name():
    """
    locate element by tag name
    :return:
    """
    url = r"https://www.51zxw.net/login"
    driver = get_driver()
    driver.get(url)
    driver.find_element_by_id("loginStr").send_keys("george")
    driver.find_element_by_name("pwd").send_keys("123456")
    driver.find_elements_by_tag_name("button")[0].click()
    sleep(3)
    driver.close()


def locate_class_name():
    """
    locate element by class name
    :return:
    """
    url =r'https://www.baidu.com/'
    driver = get_driver()
    driver.get(url)
    driver.find_element_by_class_name("s_ipt").send_keys("Python")
    sleep(3)
    driver.find_element_by_id("su").click()
    sleep(3)
    driver.close()


def locate_link_text():
    """
    locate element by link text
    :return:
    """
    url = "https://www.51zxw.net/"
    driver = get_driver()
    driver.get(url)
    driver.find_element_by_link_text("程序设计").click()
    sleep(3)
    driver.close()


def locate_partial_link_text():
    """
    locate element by link text
    :return:
    """
    url = "https://www.51zxw.net/"
    driver = get_driver()
    driver.get(url)
    driver.find_element_by_partial_link_text("室内").click()
    sleep(3)
    driver.close()


def locate_xpath():
    """
    locate by xpath
    :return:
    """
    url = r'https://www.baidu.com/'
    driver = get_driver()
    driver.get(url)
    # driver.find_element_by_xpath("//input[@id='kw']").send_keys("Python")
    driver.find_element_by_xpath("//input[@class='s_ipt']").send_keys("Python")
    sleep(3)
    # driver.find_element_by_xpath("//input[@id='su']").click()
    driver.find_element_by_xpath("//input[@value='百度一下']").click()
    sleep(3)
    driver.close()


def locate_xpath_relative():
    """
    locate xpath
    :return:
    """
    url = r'https://www.51zxw.net/'
    driver = get_driver()
    driver.get(url)

    # driver.find_element_by_xpath("//div[@id='courseTypes']//div[2]/a[.='Windows']").click()
    driver.find_element_by_xpath("//div[@id='courseTypes']/div/div/div[2]/a[.='Windows']").click()
    # logical combination positioning
    # driver.find_element_by_xpath("//div[@id='kw']"/input[@id='name' and @value='hello']).click()
    sleep(3)
    driver.close()


def locate_css():
    """
    locate css
    :return:
    """
    url = r"https://www.baidu.com"
    driver = get_driver()
    driver.get(url)
    # locate by id
    driver.find_element_by_css_selector("#kw").send_keys("Python")
    sleep(3)
    # locate by class
    driver.find_element_by_css_selector(".s_ipt").send_keys("Hello")
    sleep(2)
    # locate by property
    driver.find_element_by_css_selector("#su").click()
    # css locator use > to differentiate hierarchy to property behind node like form#loginForm
    driver.find_element_by_css_selector("form#loginForm>ul>input").send_keys("Hello")
    sleep(3)
    driver.close()


def locate_select():
    """
    locate select
    :return:
    """
    url = r'https://www.51zxw.net/'
    driver = get_driver()
    driver.get(url)
    # method 1use value
    driver.find_element_by_css_selector("[value='2']").click()
    # method2 use option
    driver.find_elements_by_tag_name('option')[1].click()
    # method 3
    select = Select(driver.find_element_by_css_selector("[name='cookieDate']"))
    select.select_by_index(1)
    select.select_by_value('2')
    select.select_by_visible_text("留两天")


if __name__ == "__main__":
    # basic_operation()
    # locate_id_name()
    # locate_tag_name()
    # locate_class_name()
    # locate_link_text()
    # locate_partial_link_text()
    # locate_xpath()
    # locate_xpath_relative()
    locate_css()