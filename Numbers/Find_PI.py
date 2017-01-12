import math
import string
#get input
n = int(input("Enter the number N\n"))+1
assert n < 100
#n = int(n.split()[0])
n = str(n)
temp = "."+n

#prompt the option for either PI or e
i = int(input("Enter 0 for PI, 1 for e\n"))
if i==0:
    p = math.pi
else:
    p = math.e


print(p.__format__(temp))
