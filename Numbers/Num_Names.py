# Number Names - Show how to spell out a number in English. You can use a preexisting implementation or roll your own,
# but you should support inputs up to at least one million (or the maximum value of
# your language's default bounded integer type, if that's less).
# Optional: Support for inputs other than positive integers (like zero, negative integers, and floating-point numbers).
#[] for list
#() for tuple
#{} for dictionary

num_unit = ('','one','two','three','four','five','six','seven','eight','nine')
num_special ={'11':'eleven','12':'twelve','13':'thirteen','14':'fourteen','15':'fifteen',
              '16':'sixteen','17':'seventeen','18':'eighteen','19':'nineteen'
              }
num_tenth =('zero','ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety')
num_hund =('hundred ','hundreds ')
num_thou =('thousand ','thousands ')

n = (input("Enter N"))
c = n[:]
TEN=0
THOU=0
HUND=0
if str.__len__(n)>=4:
    THOU = int(c[str.__len__(n)-4])
if str.__len__(n)>=3:
    HUND = int(c[str.__len__(n)-3])
if str.__len__(n)>=2:
    TEN = int(c[str.__len__(n)-2])
UNIT = int(c[str.__len__(n)-1])
if THOU > 1:
    print(num_unit.__getitem__(THOU)+' '+num_thou.__getitem__(1),end="")
elif THOU ==1:
    print(num_unit.__getitem__(THOU)+' '+num_thou.__getitem__(0),end="")
if HUND>1:
    print(num_unit.__getitem__(HUND)+' '+num_hund.__getitem__(1),end="")
elif HUND == 1:
    print(num_unit.__getitem__(HUND)+' '+num_hund.__getitem__(0),end="")
# for calc 1~19 excluding 10
temp = int(str(TEN)+str(UNIT))
if temp > 10:
    if temp < 20:
        print(num_special.get((str(TEN)+str(UNIT))))
    elif int(str(TEN)+str(UNIT))%10==0:#10,20,30.etc
            print(num_tenth.__getitem__(int(int(n)/10)))
    else:#20~99 excluding 10 dividable nums
        print(num_tenth.__getitem__(TEN)+' '+num_unit.__getitem__(UNIT))
else:
    print(num_unit.__getitem__(UNIT))


