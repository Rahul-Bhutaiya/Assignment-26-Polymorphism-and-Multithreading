"""
Write a python script to create two Threads. First thread will print all Even numbers
and Second thread will print all Odd numbers till 100.
"""
from threading import Thread
from time import sleep

class odd(Thread):
    def run(self):
        for x in range(1,100,2):
            print(x)
            sleep(2)

class even(Thread):
    def run(self):
        for x in range(2,101,2):
            print(x)
            sleep(2)

odd_obj=odd()
even_obj=even()

odd_obj.start()
sleep(1)
even_obj.start()

odd_obj.join()
odd_obj.join()

print('Executed')
