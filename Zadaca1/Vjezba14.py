def isPrime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5) +1):
        if n % i == 0:
            return False
        
    return True

print(isPrime(7))  
print(isPrime(6))  

def primes_in_range(start, end):
    primes= []
    for i in range(start, end +1):
        if isPrime(i):
            primes.append(i)
    return primes

print(primes_in_range(1, 10))