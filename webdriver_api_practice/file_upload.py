# -*-coding:utf-8 -*-
# File :file_upload.py
# Author:George
# Date : 2019/10/11
# motto: Someone always give up while someone always try!
from automated_testing.webdriver_api_practice.getDriver import get_driver
from time import sleep


def upload_file_demo():
    """

    :return:
    """
    image_path = r'F:\Personal_Folder\Imagies\jiesi.png'
    url = r'https://www.baidu.com'
    driver = get_driver()
    driver.get(url)
    # locate upload button
    driver.find_element_by_xpath("//span[@class='soutu-btn']").click()
    sleep(2)
    driver.find_element_by_css_selector(".upload-pic").send_keys(image_path)
    sleep(10)
    driver.close()


if __name__ == "__main__":
    upload_file_demo()
