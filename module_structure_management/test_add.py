# -*-coding:utf-8 -*-
# File :test_add.py
# Author:George
# Date : 2019/10/12
# motto: Someone always give up while someone always try!
from operation import Operation
from startEnd import StartEnd
import unittest


class AddTest(StartEnd):

    @classmethod
    def setUpClass(cls):
        print("AddTest class begin to test...")

    def test_add(self):
        operation = Operation(5, 3)
        result = operation.add()
        self.assertEqual(result, 8)

    @unittest.skip("No need this testcase!")
    def test_add_1(self):
        operation = Operation(5, 5)
        result = operation.add()
        self.assertEqual(result, 10)

    @unittest.skipIf(3 > 2, "3 is bigger then 2")
    def test_add_2(self):
        operation = Operation(5, 5)
        result = operation.add()
        self.assertEqual(result, 10)

    @unittest.skipUnless(3 < 2, "3 is bigger then 2")
    def test_add_3(self):
        operation = Operation(5, 5)
        result = operation.add()
        self.assertEqual(result, 10)

    @unittest.expectedFailure
    def test_add_4(self):
        operation = Operation(5, 5)
        result = operation.add()
        self.assertEqual(result, 9)
    # class method
    @classmethod
    def tearDownClass(cls):
        print("AddTest class finish test...")



