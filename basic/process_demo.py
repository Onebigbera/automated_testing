# -*-coding:utf-8 -*-
# File :process_demo.py
# Author:George
# Date : 2019/10/9
# motto: Someone always give up while someone always try!
import threading
from multiprocessing import Process
import os
import time


def do_work(name):
    """
    :param name: worker name
    :return:
    """
    print("do_work function subprocess，and the subprocess ID is {} and it's parent process ID nis {},"
          "and it's threading ID is {} and the time is {}".format(os.getpid(), os.getppid(), threading.get_ident(),time.ctime()))


def do_sleep(name):
    """
    :param name: sleeper name
    :return:
    """
    print("do_sleep function subprocess，and the subprocess ID is {} and it's parent process ID nis {},"
          "and it's threading ID is {}, and the time is {}".format(os.getpid(), os.getppid(), threading.get_ident(), time.ctime()))
    print("{} go to sleep for a while".format(name))
    time.sleep(3)
    print("after 3 seconds...")
    print("{} has wake up!".format(name))


def main(name):
    print("main function subprocess，and the subprocess ID is {} and it's parent process ID nis {},"
          "and it's threading ID is {}".format(os.getpid(), os.getppid(), threading.get_ident()))
    process_work = Process(target=do_work, args=(name,), kwargs={})
    process_sleep = Process(target=do_sleep, args=(name,), kwargs={})
    # Judge whether the process is active
    print(process_work.is_alive())
    if not process_work.is_alive():
        process_work.start()
        process_sleep.start()
    if process_sleep.is_alive():
        process_work.join()
        process_sleep.join()
    process_work.terminate()
    process_sleep.terminate()
    print(process_sleep.is_alive())


if __name__ == "__main__":
    name = "George"
    # do_work(name)
    # do_sleep(name)
    main(name=name)