# -*-coding:utf-8 -*-
# File :unittest_demos.py
# Author:George
# Date : 2019/10/12
# motto: Someone always give up while someone always try!
"""
    basic Operation of unittest
"""
from automated_testing.unittest_basic.basic_class import Operation
import unittest


class TestOperation(unittest.TestCase):
    def setUP(self):
        """make preparation for all test case"""
        print("=====Begin test=====")

    def test_add(self):
        """test add method of Operation class"""
        operation = Operation(3, 4)
        result = operation.add()
        self.assertEqual(result, 7)

    def test_add_1(self):
        operation = Operation(10, 3)
        result = operation.add()
        self.assertNotEqual(result, 12)

    def test_assertion(self):
        a = "Hello"
        b = "Hello"
        self.assertIs(a, b)

    def test_assertion_1(self):
        num = 3
        list = [1, 2, 3]
        self.assertIn(num, list)

    def test_assertion_2(self):
        operation = Operation(3, 4)
        self.assertIsInstance(operation, Operation)

    def test_assert_3(self):
        num = 3 + 5
        self.assertTrue(num > 6)

    def tearDown(self):
        """reset test environment"""
        print("=====Finish test=====")


class TestOperationSub(unittest.TestCase):
    def setUp(self):
        print("=====Begin test=====")

    def test_sub(self):
        operation = Operation(4, 2)
        result = operation.sub()
        self.assertEqual(result, 2)

    def tearDown(self):
        print("=====Finish test=====")


if __name__ == "__main__":
    # instantiation a TestSuite object
    suite = unittest.TestSuite()

    # TestSuite to load test case
    # suite.addTests([TestOperation("test_add"), TestOperation("test_add_1")])
    suite.addTest(TestOperation("test_add"))
    suite.addTest(TestOperation("test_add_1"))

    # add Another Class test case into the test suite
    suite.addTest(TestOperationSub("test_sub"))
    # instantiation runner object
    runner = unittest.TextTestRunner
    # run test suite
    runner.run(suite)





