# Collatz Conjecture - Start with a number n > 1. Find the number of steps
# it takes to reach one using the following process:
# If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.


def find_step(i):
    step = 0
    while i > 0:
        if i == 1:
            print(step)
            break
        elif i % 2 == 0:  # even
            step += 1
            i = int(i / 2)
        else:  # odd
            i = i * 3 + 1
            step += 1

if __name__ == '__main__':
    for i in range(1,100000):
        print(i,end=" and step is : ")
        find_step(i)