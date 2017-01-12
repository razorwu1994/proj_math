import math
def isHappyNum(num):
    if num == 1:
        return True
    else:
        temp = num
        i= 0
        sum = 0
        while i !=4:
            sum += (num % 10)
            num = int(num/10)
            i += 1
        if sum == temp:
            return False
        else:
            return isHappyNum(sum)

if __name__ == '__main__':

    for i in range(2,3000):
        if isHappyNum(i):
            print(str(i))

    # TRUE_Count = 0
    # i = 1
    # while i > 0:
    #     if isHappyNum(i):
    #         TRUE_Count+=1
    #         print(i)
    #     elif TRUE_Count > 8:
    #         break
    #     i += 1
