"""
Write a python script to create a clock where 1st thread will print the current time
every second and 2nd will print “1 Minute Completed” after every 1 minute.
"""

from threading import Thread
from datetime import datetime
from time import sleep

class Thread1(Thread):
    def run(self):
        while True:
            current_time=datetime.now()
            print(current_time.strftime("%H:%M:%S"))
            sleep(1)

class Thread2(Thread):
    def run(self):
        while True:
            curr_time=datetime.now()
            if curr_time.second==00:
                sleep(1)
                print('1 Minute Completed')
                sleep(59)
obj=Thread1()
obj2=Thread2()

obj.start()
obj2.start()