'''
SPY GAME:
Write a function that takes in a list of integers and returns True 
if it contains 007 in order
 spy_game([1,2,4,0,0,7,5]) --> True
 spy_game([1,0,2,4,0,5,7]) --> True
 spy_game([1,7,2,0,4,5,0]) --> False
 '''
 
 #SOLUtXION ! ~
 
def spy_game(value):
    code= [0,0,7,'x']
     
    for num in value:
        if num == code[0]:
            code.pop(0)
    return len(code)== 1     #it means that 0, then 0, then 7 shall be popped out
                             #from the list and only a string of length 1 left after 
                             #completion of loop, means 1 time gone through loop.
                                
print(spy_game([1,2,3,3,4,0,7]))