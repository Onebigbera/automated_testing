# -*-coding:utf-8 -*-
# File :xml_handler_demo.py
# Author:George
# Date : 2019/10/9
# motto: Someone always give up while someone always try!
from xml.dom import minidom


def xml_handler(file):
    """
    get element node
    :param file:
    :return:
    """
    dom = minidom.parse(file)
    root = dom.documentElement

    # root is element node
    print(root.nodeName)
    print(root.nodeValue)
    # 1 stand for element node ,2 stand for property node
    print(root.nodeType)


def get_xml_data(file):
    """
    get text node
    :param file:
    :return:
    """
    dom = minidom.parse(file)
    root = dom.documentElement
    # names、ages、citys are text nodes
    names = root.getElementsByTagName('name')
    ages = root.getElementsByTagName('age')
    citys = root.getElementsByTagName('city')
    for item in range(4):
        # get item value
        print(names[item].firstChild.data)
        print(ages[item].firstChild.data)
        print(citys[item].firstChild.data)


def property_node(file):
    """
    get property node
    :return:
    """
    dom = minidom.parse(file)
    root = dom.documentElement
    logins = root.getElementsByTagName("login")
    for item in range(2):
        username = logins[item].getAttribute("username")
        password = logins[item].getAttribute("password")
        print("username is {}, and password is {}".format(username, password))

    students = root.getElementsByTagName("student")
    for student in students:
        node_name = student.nodeName
        node_value = student.nodeValue
        node_type = student.nodeType
        print(node_name)
        print(node_value)
        print(node_type)


if __name__ == "__main__":
    file_path = './data/School.xml'
    print("=====get element node=====")
    xml_handler(file_path)
    print("=====get text node=====")
    get_xml_data(file_path)
    print("=====get property node=====")
    property_node(file_path)
