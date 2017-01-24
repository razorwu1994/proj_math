


f = open("G:\GitFolder\proj_math\demo","r")
string = f.readline()
string += f.readline()
print(string)
sum =0;
for i in range(0,string.__len__()):
    if  string[i].isspace():
        sum+=1

print("words: "+str(sum+1))