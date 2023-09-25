'''
FIND 33:
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False
'''

def has_33(j):
    
    for i in range(0, len(j)-1):
        if j[i]== 3 and j[i+1]==3:
            return True
    else:
        return False
print(has_33([1,3,5,3,5,0,3,3]))
    