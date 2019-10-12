# -*-coding:utf-8 -*-
# File :set_up_tear_down.py
# Author:George
# Date : 2019/10/12
# motto: Someone always give up while someone always try!
"""
    To handler the setUp and tearDown methods
    to inherit the class with setUp and tearDown methods set
"""
from automated_testing.unittest_basic.basic_class import Operation
import unittest


class SetUPTearDown(unittest.TestCase):
    def setUp(self):
        print("===Test begin!===")

    def tearDown(self):
        print("===Test finished!===")


class TestOperation(SetUPTearDown):
    def test_add(self):
        operation = Operation(4, 5)
        result = operation.add()
        self.assertEqual(result, 9)

    def test_add_1(self):
        operation = Operation(4, 4)
        result = operation.add()
        self.assertEqual(result, 8)


class TestOperationSub(SetUPTearDown):
    def test_sub(self):
        operation = Operation(5, 2)
        result = operation.sub()
        self.assertEqual(result, 3)

    def test_sub_1(self):
        operation = Operation(5, 3)
        result = operation.sub()
        self.assertEqual(result, 2)


if __name__ == "__main__":
    unittest.main()