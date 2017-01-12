# The sieve of Eratosthenes is one of the most
# efficient ways to find all of the smaller primes (below 10 million or so).

def isPrime(prime):
    c = 2
    f_0 = True
    while f_0:
        if prime%c == 0:
            if c == prime:
                break
            else:
                f_0 = False
        else:
            c += 1
    return f_0

print("Find all prime numbers in fast way")
temp = []
for i in range(2,10001):
    temp.append(i)
for i in range(2,10001):
     if isPrime(i):
         print(i)
         for n in range(2,5000):
             if temp.__contains__(n*i):
                 temp.remove(n*i)
print(temp)