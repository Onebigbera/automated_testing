# -*-coding:utf-8 -*-
# File :liner model.py
# Author:George
# Date : 2019/10/11
# motto: Someone always give up while someone always try!
"""
    liner model mean the model won't interactive with other model or call other model
"""
from automated_testing.webdriver_api_practice.getDriver import get_driver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def login_action(url):
    """

    :param url: login website
    :return:
    """
    driver = get_driver()
    driver.get(url)
    driver.find_element_by_css_selector("#login_field").clear()
    # username = str(input("Please enter your account: "))
    # password = str(input("please enter your password: "))
    username = 'onebigbera'
    password = 'kaige1992!!'
    driver.find_element_by_css_selector("#login_field").send_keys(username)
    sleep(2)
    driver.find_element_by_css_selector("#password").clear()
    driver.find_element_by_css_selector("#password").send_keys(password)
    driver.find_element_by_xpath("//input[@name='commit']").click()

    # explicit wait
    element = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Pull requests')]")))
    if element:
        print("Login successfully")
    sleep(3)

    # logout action
    # driver.find_element_by_xpath("//div[@class='Header-item position-relative mr-0']//span[@class='dropdown-caret']]").click()
    driver.find_element_by_xpath("//header[@class='Header']/div[5]/details/summary").click()
    driver.find_element_by_xpath("//form[@class='logout-form']/button").click()
    # driver.find_element_by_xpath("//button[@class='dropdown-item dropdown-signout']").click()
    sleep(3)
    driver.close()


if __name__ == "__main__":
    url = r'https://github.com/login'
    login_action(url)