'''
PAPER DOLL: 
Given a string, return a string where for every character in the original there are three characters.

paper_doll('Hello') --> 'HHHeeellllllooo'
paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
'''

def paper_doll(text):
    str=''
    for char in text:
        str=str + char*3
       
    return str
    
print(paper_doll("SALAM"))




'''

lis=[]
def f(myp):
    for letter in myp:
        if 1:
            lis.append(letter)
    return lis
        
        
print(f("hammad"))
    

'''
    
