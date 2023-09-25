def func(numbers):
    return numbers%2==0

mynums=[1,2,3,4,5,6]

for iter in filter(func, mynums):
    print(iter)
    
print(list(filter(func, mynums)))

