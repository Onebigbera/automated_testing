# -*-coding:utf-8 -*-
# File :unittest_demo.py
# Author:George
# Date : 2019/10/12
# motto: Someone always give up while someone always try!
"""
    There are some demos for learning unittest
"""


class Operation(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        """

        :return: self.a + self.b
        """
        return self.a + self.b

    def sub(self):
        """

        :return: self.a - self.b
        """
        return self.a - self.b


