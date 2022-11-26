"""
Write a python script to create a user account class with 2 instance variables (userid
and balance). Create 3 user objects and add all the users using operator overloading.
"""

class user_account:
    def __init__(self,userid=None,balance=None):
        self.userid=userid
        self.balance=balance
    
    def __add__(self,obj2):
        return user_account(self.userid,self.balance+obj2.balance)
        
"""
user1=user_account('Rahul Bhutaiya',20000)
user2=user_account('Jenil Monapara',25000)
user3=user_account('Nilesh Boghara',30000)
user4=user_account('Nilesh Boghara',40000)
"""

#total=user1+user2
#total=user1.__add__(user2)

#total=user1+user2+user3
#total=(user1.__add__(user1)).__add__(user3)

#total=user1+user2+user3+user4
#total=((user1.__add__(user2)).__add__(user3)).__add__(user4)
#print(total.balance)
