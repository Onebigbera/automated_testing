# -*-coding:utf-8 -*-
# File :wait_action.py
# Author:George
# Date : 2019/10/10
# motto: Someone always give up while someone always try!
"""
    wait action
        explicit wait:
            WebDriverWait: aim at some element
            expected_conditions: expected condition
            NoSuchElementException:
        implicit wait:
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from automated_testing.webdriver_api_practice.getDriver import get_driver
from time import sleep
from selenium.common.exceptions import NoSuchElementException


def explicit_wait_demo():
    """
    explicit wait demo
    :return:
    """
    url = r'https://www.baidu.com'
    driver = get_driver()
    driver.get(url)
    driver.find_element_by_css_selector("#kw").send_keys("Python")

    element = WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.ID, 'su')))
    element.click()
    sleep(3)
    driver.close()


def implicit_wait_demo():
    """
    implicit wait wait for all the web page
    :return:
    """
    url = r"https://www.baidu.com"
    driver = get_driver()
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
    print(driver.title)
    driver.close()


if __name__ == "__main__":
    # explicit_wait_demo()
    implicit_wait_demo()



