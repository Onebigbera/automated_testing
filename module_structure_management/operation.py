# -*-coding:utf-8 -*-
# File :operation.py
# Author:George
# Date : 2019/10/12
# motto: Someone always give up while someone always try!


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
