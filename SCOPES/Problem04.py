#WAP to multiply all the numbers in the list:


def multiply(list1):
    total=1
    for items in list1:
        total=total *items
    
    return total

print(multiply([1,2,3,-4]))
        