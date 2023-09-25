#Find volume of sphere  given as 4/3πr^2

def vol(rad):
    volume=(4/3)*(3.14)*(rad**3)
    return volume

print(vol(2))

# WAP that checks wether a number is in given range

def run_check(num, low, high):
    if (num>=low) and (num<=high):
        return True
    else:
        return False

print(run_check(5,2,7))

'''or
if num in range(low,high):
    print(...)'''