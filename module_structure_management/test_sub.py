# -*-coding:utf-8 -*-
# File :test_sub.py
# Author:George
# Date : 2019/10/12
# motto: Someone always give up while someone always try!
from operation import Operation
from startEnd import StartEnd


class SubTest(StartEnd):

    @classmethod
    def setUpClass(cls):
        print("SubTest class begin to test...")

    def test_sub(self):
        operation = Operation(5, 3)
        result = operation.sub()
        self.assertEqual(result, 2)

    @classmethod
    def tearDownClass(cls):
        print("SubTest class finish test...")