#PALLINDROME OR NOT OF A STRING

def rev(str):
    #first remove Spaces between strings
    str=str.replace(' ', '')
    
    #reversing
    str=str[::-1]
    return str

print (rev("Hammad Raza Khan"))