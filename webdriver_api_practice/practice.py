# -*-coding:utf-8 -*-
# File :practice.py
# Author:George
# Date : 2019/10/11
# motto: Someone always give up while someone always try!
# -*-coding:utf-8 -*-
# File :selenium_cookie.py
# Author:George
# Date : 2018/12/5
"""
    selenium 模拟登陆码云 携带cookie免密登陆
    操作原理:
    1.模拟登陆码云平台
    2.保存登陆信息到本地cookie
    3.直接读取本地cookie 免密登陆
    操作注意: 拿到cookie的json文件后 拿到cookie的json文件 转成json文件后 去分析哪些为必要字段  比如:cookie['name'],
    cookie[valuele], .gitee.com 域名等

    """
"""
    扩展 :
    使用python-manager shell 查看自定类、函数说明文档
    切换到需要查看的文件的目录下
    进入python环境
    导入自定义的py模块  eg: import filename  (自定义py文件 filename.py)  或者 from filename import *
    help(obj)  查看自定义文档
    dir(obj)    查看对象操作方法

"""
from selenium import webdriver
import time
import json

# 自定义的本地的保存cookie的json文件
COOKIE_JSON_FILE = r'F:\Testing_Development\UnittestProjects\UnittestBasic\SeleniumOperation\TestDemo\cookies.json'


# 返回驱动的函数
def get_driver():
    return webdriver.Chrome(executable_path=r'E:\Installation_packages\Chrome_plugins\chromedriver.exe')


# 登陆gitee 返回webdriver
def gitee_cookied(url):
    """
    模拟登陆码云
    :param url: 码云的 url
    :return:
    """
    driver = get_driver()
    driver.get(url)

    # 通过 selenium 模拟登陆码云
    # 通过id寻找
    driver.find_element_by_id('user_login').send_keys('13554518280')
    time.sleep(2)
    # 通过name寻找
    driver.find_element_by_name('user[password]').send_keys('kaige1992!!')
    time.sleep(2)
    # 通过xpath寻找 定位到点击登陆按钮
    # driver.find_element_by_xpath("//div/input[@name='commit']").click()
    # 两种方法都可以
    driver.find_element_by_name('commit').click()
    time.sleep(3)
    print(driver.get_cookies())
    print("获取到的cookie类型是: ", type(
        driver.get_cookies()))  # <class 'list'> 通过 driver.get_cookies() 方法得到的对象是一个包含多个字典的列表 其形式如下：
    """
    [
       {'domain': 'gitee.com', 'httpOnly': True, 'name': 'aliyungf_tc', 'path': '/', 'secure': False, 'value': 'AQAAADBuoTht5wMA5Fmadc9pcvMb8CHk'},
       {'domain': 'gitee.com', 'expiry': 2176875300.798951, 'httpOnly': False, 'name': 'oschina_new_user', 'path': '/', 'secure': False, 'value': 'false'},
       {'domain': '.gitee.com', 'httpOnly': True, 'name': 'gitee-session-n', 'path': '/', 'secure': False}, 
       ...
    ]
    """
    # 返回携带cookie信息的driver 此时的 driver 是携带 cookie 的
    return driver


# 获取cookie信息
def get_cookie(driver):
    """

    :param driver:
    :return:
    """
    # 获取登陆后的服务器cookie
    cookie_dict = driver.get_cookies()
    # 将json字典对象转化为python字符串
    cookie_str = json.dumps(cookie_dict)
    print("通过json.dumps() 方法后类型为 : ", type(cookie_str))
    with open(COOKIE_JSON_FILE, 'w', encoding='utf-8') as f:
        # 打开文件 将cook_str写入文件中
        f.write(cookie_str)

    # 可以选择性返回结果
    return COOKIE_JSON_FILE


# 携带cookie进行免密码登陆
def login_without_account(driver, url):
    # (1)登陆码云  首先要驱动去访问接口  获取cookie信息
    driver.get(url)

    # (2)删除第一次连接服务器时的残留本地的cookie
    driver.delete_all_cookies()

    # (3)读取保存在本地的cookie信息
    with open(COOKIE_JSON_FILE, 'r', encoding='utf-8') as f:
        # 读取出json字符串 读取出来为 json 字符串
        json_content = f.read()

        # 将json文本字符串转化为 python中的对象列表
        listjsonCookies = json.loads(json_content)

    # (4) 将cookie添加到driver里面 add_cookiie
    for cookie in listjsonCookies:
        """
        需要拿出cookie文件进行json在线解析 了解json中都有哪些字段需要提交

        """
        # 也是按照添加的字典 按照字典的格式  key 不更改， value 按照 cookie 中 json 文件进行赋值配置
        driver.add_cookie(
            {
                # 需要自己按照格式添加cookie中需要的字段  仿造一模一样的cookie
                "domain": cookie['domain'],
                "httpOnly": cookie['httpOnly'],
                "name": cookie['name'],
                "value": cookie['value'],
                "path": cookie['path'],
            }
        )
    # (5)将加入lcookie信息的driver再登陆
    driver.get(url)


def login_wait(driver):
    time.sleep(10)
    # 驱动离开 释放资源
    driver.close()
    driver.quit()


url = 'https://gitee.com/login'


def main():
    # 生成携带cookie的driver
    driver_g = gitee_cookied(url)

    # 生成cookie文件 在生成后就可以不需要
    get_cookie(driver_g)

    # 免密码登陆
    # 提取携带cookie信息驱动中的cookie
    login_without_account(driver_g, url)

    # 驱动关闭
    login_wait(driver_g)


if __name__ == "__main__":
    main()
