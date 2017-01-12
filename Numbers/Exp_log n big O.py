# Fast Exponentiation - Ask the user to enter 2 integers a and b and output a^b (i.e. pow(a,b))
# in O(lg n) time complexity.
# a ^ b, a * (b/2+b/4+b/8...) =((2^n-1)*b/2^n)+(1/2^n)
# for int i = 1;i<
import math
a = int(input("Enter a "))
b = int(input("Enter b "))
c = b
exp = c
if ((b & (b - 1)) == 0) and b != 0:
    #b is the pow of 2
        c /= 2
elif (b & (b - 1)) != 0:
    for i in range(0,100):
        if math.pow(2,i) > b:
            c = math.pow(2,i-2)#like c /= 2  pow(2,i-1) /2 = pow (2,i - 2)
            exp = i-1
            break

temp_exp = a

while c > 0 :
    temp_exp *= temp_exp
    c = int(c/2)
t = b - int(math.pow(2,exp))

for t in range(1,t+1):
    temp_exp *= a
print(temp_exp)