"""
Write a python script to check whether a given number is prime or armstrong number
using 2 different threads.
"""
from threading import Thread
from time import sleep
"""
#method : 1
class prime(Thread):
    def run(self):
        val=int(input('Enter The Value Which You Want To Check : '))
        for x in range(2,val):
            if val%x==0:
                print(val,'is Not A Prime Number')
                break
        else:
            print(val,'is a Prime Number')

class armstrong(Thread):
    def run(self):
        val=input('Enter The Value Which You Want To Check : ')
        total=0
        for x in val:
            total+=int(x)**3
        if int(val)==total:
            print(val,'is an Armstrong Number')
        else:
            print(val,'is Not an Armstrong Number')
"""
#Method : 2
value=int(input('Enter The Value : '))

def prime():
    for x in range(2,value):
        if value%x==0:
            print(value,'is Not a Prime Number')
            break
    else:
        print(value,'is a Prime Number')

def armstrong():
    total=0
    for x in str(value):
        total+=int(x)**3
    if value==total:
        print(value,'is an Armstrong Number')
    else:
        print(value,'is Not an Armstrong Number')


prime_thread=Thread(target=prime)
armstrong_thread=Thread(target=armstrong)
prime_thread.start()
sleep(1)
armstrong_thread.start()