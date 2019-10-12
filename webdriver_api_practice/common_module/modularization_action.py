# -*-coding:utf-8 -*-
# File :modularization_action.py
# Author:George
# Date : 2019/10/11
# motto: Someone always give up while someone always try!
from automated_testing.webdriver_api_practice.getDriver import get_driver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Login(object):
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def user_login(self):
        self.driver.get(self.url)
        self.driver.find_element_by_css_selector("#login_field").clear()
        # username = str(input("Please enter your account: "))
        # password = str(input("please enter your password: "))
        username = 'onebigbera'
        password = 'kaige1992!!'
        self.driver.find_element_by_css_selector("#login_field").send_keys(username)
        sleep(2)
        self.driver.find_element_by_css_selector("#password").clear()
        self.driver.find_element_by_css_selector("#password").send_keys(password)
        self.driver.find_element_by_xpath("//input[@name='commit']").click()

        # explicit wait
        element = WebDriverWait(self.driver, 20, 0.5).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Pull requests')]")))
        if element:
            print("Login successfully")

    def user_logout(self):
        # logout action
        # driver.find_element_by_xpath("//div[@class='Header-item position-relative mr-0']//span[@class='dropdown-caret']]").click()
        # todo: to locate the summary the xpath path is incorrect
        self.driver.find_element_by_xpath("//header[@class='Header']/div[5]/details/summary[1]").click()
        self.driver.find_element_by_xpath("//form[@class='logout-form']/button").click()
        # driver.find_element_by_xpath("//button[@class='dropdown-item dropdown-signout']").click()
        sleep(3)
        self.driver.close()


if __name__ == "__main__":
    url = r'https://github.com/login'
    driver = get_driver()
    # login and logout share the same driver
    login_handler = Login(driver, url)
    login_handler.user_login()
    login_handler.user_logout()
