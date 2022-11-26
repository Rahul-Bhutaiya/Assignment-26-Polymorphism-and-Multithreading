"""
Write a python script to create a to print the above user account object using operator
overloading (hint __str__ method).
"""

class user_account:
    def __init__(self,userid=None,balance=None):
        self.userid=userid
        self.balance=balance
    
    def __add__(self,obj2):
        return user_account(self.userid,self.balance+obj2.balance)

    def __str__(self):
        return str(self.balance)

""" 
user1=user_account('Rahul Bhutaiya',20000)
user2=user_account('Jenil Monapara',25000)
user3=user_account('Nilesh Boghara',30000)
user4=user_account('Nilesh Boghara',40000)

print(user1+user2+user4+user3)
"""
