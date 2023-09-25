# WAP to return unique elemnts.
Sample_set= [1,1,1,1,1,1,2,2,2,2,2]
Unique_List=[]

def unique_list(Unique_List):
    return (list(set(Unique_List)))
  
print(unique_list(Sample_set))

           #OR
           
def unique_list(Sample_set):
    seen=[]
    for number in Sample_set:
        if number not in seen:
            seen.append(number)
    return seen
print(unique_list(Sample_set))