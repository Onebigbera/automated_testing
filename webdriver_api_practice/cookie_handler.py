# -*-coding:utf-8 -*-
# File :cookie_handler.py
# Author:George
# Date : 2019/10/11
# motto: Someone always give up while someone always try!
"""

"""
from automated_testing.webdriver_api_practice.getDriver import get_driver
from time import sleep
import json


def cookie_handler():
    """

    :return:
    """
    driver = get_driver()
    url = r"https://www.51zxw.net/Show.aspx?cid=615&id=60850"
    driver.get(url)
    cookie = driver.get_cookies()
    sleep(3)
    print(cookie)
    cookie_directory = r'F:\Testing_Development\UnittestProjects\automated_testing\automated_testing\webdriver_api_practice\cookie_data'
    with open(cookie_directory + '\\' + ".51zxw_json.json", 'w') as f:
        # change the json object to json object and write to file
        json.dump(cookie, f)
        # f.write(json.dumps(cookie))
    print(type(cookie))
    for item in cookie:
        print("name is {} and value is {}".format(item['name'], item['value']))
    sleep(3)
    # add cookie
    driver.add_cookie({'name': '51zxw', 'value': 'www.51zxw.com'})
    driver.get(url)
    driver.close()


if __name__ == "__main__":
    cookie_handler()