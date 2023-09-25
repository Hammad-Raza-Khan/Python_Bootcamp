'''def square(num):
    return num**2

print(square(3))'''
nums=[1,2,3,4,10]
print(list(map(lambda num: num**2,nums)))

names=['abc', 'def', 'hgi']
print(list(map(lambda str:str[::-1], names)))

