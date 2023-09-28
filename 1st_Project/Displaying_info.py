#Creating basic tic tac toe !

#Step 1- Enroll them into a function
line1=[' ', ' ', ' ']
line2=[' ', ' ', ' ']
line3=[' ', ' ', ' ']



#2 Now Print -

def func(line1,line2,line3):
    print(line1)
    print(line2)
    print(line3)
print(func(line1,line2,line3))

'''#5 Play by inserting values at Index !
line2[1]='X'
line1[2]='X'
line3[0]='O'
line1[0]='O'
line2[0]='O'''

# Taking input 

#posxn= int (input ("Choose an index position: "))


# Checing if the input is valid or not-
# METHOD 1
posxn=int (input ("Choose an index position: "))

if type(posxn)==int:
    print("Valid")
else:
    print("Invalid")
    
#METHOD 2
def int (value):
    try:
        val = int(posxn)
    except ValueError:
        print ("Valid")
        
print(int("invalid"))




