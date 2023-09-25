'''
COUNT PRIMES: Write a function that returns the number of prime numbers that 
exist up to and including a given number
count_primes(100) --> 25

By convention, 0 and 1 are not prime.
'''

def count_primes(p):
    if p<2:
        return 0
    
    # making a prime placeholder to hold & store prime numbers
    prime=[2]
    # making a counter which searches up Prime Numbers UP to P
    x=3
    
    #Now, first checking if x is prime or not; also by mentioning prime as 2, we can start with 3 and
    # iterate/skip every 2 numbers since they would be even and therefore, divisible by 2
    while x<=p:
        for y in prime:
            if x%y==0:
                x+=2
                break
        else:
            prime.append(x)
            x+=2
    print(prime)
    return len(prime)

print(count_primes(100))
        
    