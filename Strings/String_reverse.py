string = input("Enter string\t")
temp=""
i = str(string).__len__()-1
while i >=0:
    temp+=str(string).__getitem__(i)
    i-=1
print(temp)