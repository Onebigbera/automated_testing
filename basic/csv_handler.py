# -*-coding:utf-8 -*-
# File :csv_handler.py
# Author:George
# Date : 2019/10/9
# motto: Someone always give up while someone always try!
"""
    simple show how to deal with csv file
"""
import csv


def csv_reader_demo(file):
    """csv reader with csv file data"""
    with open(file, 'r') as f:
        csv_file_data = csv.reader(f)
        for item in csv_file_data:
            print(" {} {} {}".format(item[0], item[1], item[2]))


def csv_writer_demo(file, data):
    """csv writer with"""
    with open(file, "a", newline="") as f:
        # instantiation a csv writer
        csv_writer = csv.writer(f, dialect='excel')
        csv_writer.writerow(data)


if __name__ == "__main__":
    data_file = './data/student_info.csv'
    csv_reader_demo(data_file)
    data = ["Susan", 22, "Music"]
    csv_writer_demo(data_file, data)
    print("======After write new row=====")
    csv_reader_demo(data_file)

