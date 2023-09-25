'''
PRINT BIG:
Write a function that takes in a single letter, and returns a 5x5 
representation of that letter
print_big('a')

out:   *  
      * *
     *****
     *   *
     *   *
     
     
HINT: Consider making a dictionary of possible patterns, 
and mapping the alphabet to specific 5-line combinations of patterns.
For purposes of this exercise, it's ok if your dictionary stops at "E".

'''

def print_big(a):
    dict= {1: '  *  ', 2:'*   *', 3:'*   *', 4:'****', 5:'*****', 6: '   * ',7:' *   ', 8:'*  * ', 9:'*   '}
    alphabet= {'A': [1,2,3,5,3,3,], 'B': [9,3,8,2,1,2,3,8,2,1],'C': [8,9,9,9,9,8] , 'D': [4,2,8,3,8,7,9] , 'E': [5,9,9,9,9,9,5]}
    
    for pattern in alphabet[a.upper()]:
        print(dict[pattern])
        
print(print_big('a'))
        
        
    