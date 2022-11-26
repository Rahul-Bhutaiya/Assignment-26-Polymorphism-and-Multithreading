#Write a python script to change the name of the Thread.

from threading import current_thread
from threading import Thread

def task():
    curr_thread=current_thread()#it will give the instance of current running thread
    print('Current Thread :',curr_thread.name)#you can get the name of current running thread by instance_of_current_thread.name

    curr_thread.name=input('Enter a New Name For The Current Thread : ')#changing the name of current thread

    print('Now, The Current Thread Name is :',curr_thread.name)#Now it will print the updated thread name
    
t2=current_thread()
print("Current Working Thread :",t2.name)
t1=Thread(target=task)#when I start this t1 thread it will run task method
print('Current Thread Name : ',t1.name)#it's current name is Thread-1
t1.name='Rahul'#replacing the t1 thread name
t1.start()#t1 will execute task method