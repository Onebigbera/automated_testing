# -*-coding:utf-8 -*-
# File :test_case_order.py
# Author:George
# Date : 2019/10/12
# motto: Someone always give up while someone always try!
"""
    we can control the test case order by class name and test case name , or we can manage the order when test case was add into test suite to control test case order
"""
import unittest


class Test1(unittest.TestCase):
    def setUp(self):
        print("Test1")

    def test_b(self):
        print("test1_a")

    def test_a(self):
        print("test1_b")

    def tearDown(self):
        print("Test1")


class Test2(unittest.TestCase):
    def setUp(self):
        print("Test2")

    def test_d(self):
        print("Test2_d")

    def test_c(self):
        print("Test2_c")


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Test1("test_b"))
    suite.addTest(Test2("test_d"))
    suite.addTest(Test2("test_c"))
    suite.addTest(Test1("test_a"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
