# -*-coding:utf-8 -*-
# File :getDriver.py
# Author:George
# Date : 2019/10/10
# motto: Someone always give up while someone always try!


from selenium import webdriver
from time import sleep


def get_driver():
    """
    return driver for usage
    :return:
    """
    chrome_driver = webdriver.Chrome(executable_path=r'E:\Installation_packages\Chrome_plugins\chromedriver.exe')
    # gecko_driver = webdriver.Firefox(executable_path=r'E:\venv_packages\Browser_Drivers\geckodriver\geckodriver.exe')
    # ie_driver = webdriver.Ie(executable_path=r'E:\venv_packages\Browser_Drivers\iedriver\IEDriverServer.exe')
    # return gecko_driver
    # return ie_driver
    return chrome_driver


if __name__ == "__main__":
    url = r'https://www.51zxw.net/Show.aspx?cid=615&id=60543'
    driver = get_driver()
    driver.get(url)
    sleep(5)
    print(driver.current_url)
    print(driver.title)
    driver.close()
    driver.quit()

