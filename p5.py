#Write a python script to create 2 threads to add all the values from 1 to 100.

from threading import Thread
from time import sleep

total=0
class thread1(Thread):

    def run(self):
        for x in range(1,10,2):
            global total
            total+=x 
            sleep(2)


class thread2(Thread):

    def run(self):
        for y in range(2,11,2):
            global total
            total+=y
            sleep(2)

obj1=thread1()
obj2=thread2()

obj1.start()
sleep(1)
obj2.start()

obj1.join()
obj2.join()

print(total)