# -*-coding:utf-8 -*-
# File :gitee_cookie_login.py
# Author:George
# Date : 2019/10/11
# motto: Someone always give up while someone always try!
from automated_testing.webdriver_api_practice.getDriver import get_driver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import json
import os
import time


def login_action(url):
    """
    url:
    :return: driver with cookie data and path information
    """
    driver = get_driver()
    driver.get(url)
    username = str(input("Please enter your username:"))
    password = str(input("Please enter your password:"))

    driver.find_element_by_css_selector("#user_login").send_keys(username)
    sleep(2)
    driver.find_element_by_css_selector("#user_password").send_keys(password)
    sleep(2)
    driver.find_element_by_xpath("//div[@class='git-login-form-fields']//input[@name='commit']").click()
    sleep(3)

    element = WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH, "//strong[@class='ml-1']//a[contains(text(),'thechorus')]")))
    cookies = driver.get_cookies()
    print(type(cookies))

    # define cookie directory
    cookie_directory = r'F:\Testing_Development\UnittestProjects\automated_testing\automated_testing\webdriver_api_practice\cookie_data'
    try:
        if not os.path.exists(cookie_directory):
            os.makedirs(cookie_directory)
            print("make directory successfully")
        else:
            print("directory exists")
    except BaseException as e:
        print(e)

    with open(cookie_directory + '\\' + "gitee.json", 'w') as f:
        # change the json object to json object and write to file
        json.dump(cookies, f)
    element.click()

    sleep(3)
    # driver.close()
    return driver


def add_cookie(driver, url):
    """
    get cookie data from driver with cookies
    :param url:
    :param driver: if not with this driver domain would be make no sense
    :return:
    """
    driver = get_driver()
    driver.get(url)
    json_path = r'F:\Testing_Development\UnittestProjects\automated_testing\automated_testing\webdriver_api_practice\cookie_data\gitee.json'
    with open(json_path, 'r') as f:
        cookie_data = json.load(f)
        # print(type(cookie_data))
        # print(cookie_data)
    for item in cookie_data:
        driver.add_cookie(
            {
                'domain': item['domain'],
                'httpOnly': item['httpOnly'],
                'name': item['name'],
                'path': item['path'],
                'secure': item['secure'],
                'value': item['value']
            }
        )
    driver.get(url)

    # without account and password we can login the website  but we need to know we need the same driver
    driver.refresh()
    try:
        element = WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH, "//strong[@class='ml-1']//a[contains(text(),'thechorus')]")))
        if element:
            print("Login success with account!")
        else:
            print("Login failed!")
    except BaseException as e:
        print(e)

    # screen shot
    picture_directory = r'F:\Testing_Development\UnittestProjects\automated_testing\automated_testing\webdriver_api_practice\screen_shot'
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
        if picture_status:
            print("screen shot successfully!")
    except BaseException as e:
        print(e)
    driver.close()


if __name__ == "__main__":
    url = r"https://gitee.com/login"
    driver = login_action(url)
    sleep(5)
    add_cookie(driver, url)
