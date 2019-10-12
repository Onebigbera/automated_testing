# -*-coding:utf-8 -*-
# File :runtest.py
# Author:George
# Date : 2019/10/12
# motto: Someone always give up while someone always try!
import unittest
from BSTestRunner import BSTestRunner
from HTMLTestRunner import HTMLTestRunner
import time
from tools.send_email import send_report
import os
"""
    discover can match multi py module with the regex pattern rule,better than suite
"""
test_dir = "./"
discover = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")


if __name__ == "__main__":
    # report dictionary
    # report_dir = './test_report'
    report_dir = r'F:\Testing_Development\UnittestProjects\automated_testing\automated_testing\module_structure_management\test_report'
    report_time = time.strftime("%Y-%m-%d_%H_%M_%S")

    report_path = report_dir + '\\' + report_time + "result.html"
    with open(report_path, 'wb') as f:
        # Higher level of appearance
        runner = BSTestRunner(stream=f, title="Test Report", description='Test case result')

        # This will lead wrong result
        # runner = HTMLTestRunner(stream=f, title="Test Report", description='Test case result')
        runner.run(discover)
    time.sleep(5)


    # send test report
    lists = os.listdir(report_dir)
    print(lists)

    # get the report files order by time
    # the variable is fn(filename) and lambda function return the time file was created
    lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))
    print("the latest report is {}".format(str(lists[-1])))

    # file_path = os.path.relpath(report_path + '\\' + lists[-1])
    # print(file_path)
    lasest_file_path = os.path.join(report_dir, lists[-1])
    # lasest_file_path = report_dir + '\\' + lists[-1]

    print(lasest_file_path)
    send_report(lasest_file_path)


    # runner = unittest.TextTestRunner()
    # runner.run(discover)
