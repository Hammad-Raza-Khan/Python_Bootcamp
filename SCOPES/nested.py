#SCOPE

# An example of LEGB Rule:
# L - Local
# E - Enclosing Functions Locals
# G - Global
# B - Built-in  (open, range , etc.)

x=25 #global

def func(x):
    x=50 #Local
    return x
print(x)

lambda num:num**2 #local to lambda expression

name='Global String'

def greet():
    name='Bruce'
    print('Salam'+ name)
    
# Re-Assigning of Global Variable
#   METHODM-1 = USING FUNCTION
z=56

def fun(z):
    
    print(f'Value of z is {z}')
    
    #RE-ASSIGNMENT
    z='New Z'
    print(f'New value of z is {z}')
    return z
print(z)
print(fun(z))
