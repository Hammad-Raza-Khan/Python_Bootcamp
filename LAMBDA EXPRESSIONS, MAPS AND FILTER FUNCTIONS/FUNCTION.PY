def square(num):
    return num**2
my_nums=[1,2,3,4,5]
print(my_nums)

#Method 1 for printing = Through iterating
for item in map(square, my_nums):
    print(item)

#Method2= Using List Method
list(map(square, my_nums))
print(my_nums,"\n")
#print("\n")


def splicer(string):
    if len(string)%2==0:  
        return "Even"
    else:
        return string[0]
    
names=["Yusuf" , "Hammad", "Harib"]

print(list(map(splicer, names)))