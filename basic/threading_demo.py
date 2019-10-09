# -*-coding:utf-8 -*-
# File :threading_demo.py
# Author:George
# Date : 2019/10/9
# motto: Someone always give up while someone always try!
"""
    multi threading to sell tickets
"""
import time
import threading


ticket_num = 500
threading_lock = threading.Lock()
seller_num = 10


class SaleTicketThreading(threading.Thread):
    # init the class itself
    def __init__(self, threading_name):
        # init the parent class
        threading.Thread.__init__(self)
        # statement the threading name is private property
        self.__threading_name = threading_name

    def run(self):
        self.sale_ticket()

    def sale_ticket(self):
        global ticket_num
        while ticket_num > 0:
            print("{} sell the {} order ticket".format(self.__threading_name, ticket_num))
            threading_lock.acquire()
            ticket_num -= 1

            threading_lock.release()


def sale_ticket_main():
    """
    test sale ticket
    :return:
    """
    begin_time = time.time()
    global seller_num
    seller_list = []
    for i in range(seller_num):
        seller_threading = SaleTicketThreading("thread-{}".format(i))
        seller_list.append(seller_threading)
    [seller.start() for seller in seller_list]
    [seller.join() for seller in seller_list]
    end_time = time.time()
    process_time = end_time - begin_time
    print("The cost time is {}".format(process_time))


if __name__ == "__main__":
    sale_ticket_main()









