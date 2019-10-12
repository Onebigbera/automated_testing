# -*-coding:utf-8 -*-
# File :startEnd.py
# Author:George
# Date : 2019/10/12
# motto: Someone always give up while someone always try!
import unittest


class StartEnd(unittest.TestCase):
    def setUp(self):
        print("===Test begin===")

    def tearDown(self):
        print("===Test finish===")
