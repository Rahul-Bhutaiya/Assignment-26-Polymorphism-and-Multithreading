#Write a python script to join 2 threads after printing completing the first Question(p4.py)

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
