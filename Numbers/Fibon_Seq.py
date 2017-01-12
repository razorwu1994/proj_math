
if __name__ == '__main__':

    n = int(input("Enter the number N, Please note that N must be greater than 3 \n"))
    F_st = 1
    S_ec = 1
    print("1\t" * 2, end="")
    if n < 3:
        print("")
    else:
        while n - 2 != 0:
            temp = F_st + S_ec
            print(str(temp).format("#####.6"), end="\t")
            F_st = S_ec
            S_ec = temp
            n -= 1

