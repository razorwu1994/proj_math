import math
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

def primeFinder(N):
    dvd = 2 # least prime num
    while N !=1:
        if N%dvd == 0:
            N/=dvd
            print(str(dvd)+"\t",end="")
        else:
            dvd+=1


i = int(input("\nEnter N for test prime factor\n"))
primeFinder(i)
#print(isPrime(i))


#Start from prime number 2
flag = True
prime = 2
while flag:
    i=int(input("\nEnter 1 to find prime number \n"))
    if i != 1:
        flag = False
    else:
        sentinel = isPrime(prime)
        while sentinel == False:
            prime += 1
            sentinel = isPrime(prime)
        print(prime,end="\t")
        prime+=1
else:
    pass