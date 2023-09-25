#WAP that accepts a string that accepts a string and calculates the number of upper case letters and lower case letters.

def up_low(string):
    
    lowercase=0
    uppercase=0
    
    for char in string:
        if char.isupper():
            uppercase+=1
            
        
        elif char.islower():
            lowercase+=1
        else: pass
    print(f"Number of UPPER-CASE: {uppercase}")
    print(f"Number of lower-CASE: {lowercase}")


string=input()
print(up_low(string))
        #or you can also use dictionary to store values of UPPERCASE & LOWERCASE