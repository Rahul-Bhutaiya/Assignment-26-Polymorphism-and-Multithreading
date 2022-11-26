#Write a python script to create 5 threads to fill a list with random numbers till 100.

from random import randrange
from threading import Thread
from time import sleep

list_var=[]
class thread1(Thread):
    def run(self):
        for x in range(1,6):
            list_var.append(randrange(1,21))
            sleep(8)

class thread2(Thread):
    def run(self):
        for x in range(1,6):
            list_var.append(randrange(21,41))
            sleep(8)

class thread3(Thread):
    def run(self):
        for x in range(1,6):
            list_var.append(randrange(41,61))
            sleep(8)

class thread4(Thread):
    def run(self):
        for x in range(1,6):
            list_var.append(randrange(61,81))
            sleep(8)

class thread5(Thread):
    def run(self):
        for x in range(1,6):
            list_var.append(randrange(81,101))
            sleep(8)

obj1=thread1()
obj2=thread2()
obj3=thread3()
obj4=thread4()
obj5=thread5()

obj1.start()
sleep(1)
obj2.start()
sleep(1)
obj3.start()
sleep(1)
obj4.start()
sleep(1)
obj5.start()
sleep(1)

# obj1.join()
# obj2.join()
# obj3.join()
# obj4.join()
obj5.join()

print(list_var)