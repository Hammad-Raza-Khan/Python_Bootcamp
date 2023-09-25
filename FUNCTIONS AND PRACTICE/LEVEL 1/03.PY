'''Given two integers, return True if the sum of the integers is 20 or if 
one of the integers is 20. If not, return False
makes_twenty(20,10) --> True
makes_twenty(12,8) --> True
makes_twenty(2,3) --> False'''

def fj(n,m):
    a=[]
    b=[]
    
    if (a==20 or b==20) or (a+b==20):
        return True
    else:
        return False
a=int(input("Enter a"))
b=int(input("Enter b"))
print(fj(a,b))

    
    