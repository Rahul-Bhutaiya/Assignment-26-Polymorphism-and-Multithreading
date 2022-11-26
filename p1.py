"""
Write a python script to multiple 2 or 3 or 4 numbers with a single multiply method in
a class using method overloading.
"""

class multiply:
    @staticmethod
    def mul(v1=None,v2=None,v3=None,v4=None):
        if v4!=None:
            return v1*v2*v3*v4
        elif v3!=None:
            return v1*v2*v3
        elif v2!=None:
            return v1*v2
        else:
            return v1
        
#print(multiply.mul(2,3,4,5))