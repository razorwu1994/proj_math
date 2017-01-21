# (Ex.: "banana" would yield anana-bay).
string = str(input("enter string\t")).lower()
vowel_count =0

initial = str(string).__getitem__(0)
vowel = ('a','e','i','o','u')
for i in range(0,str(string).__len__()):
    if vowel.__contains__(string.__getitem__(i)):
        vowel_count+=1
print(str(vowel_count)+"vowels")

teststr = string[:].lower()
test=""
i = teststr.__len__()-1
while i >=0:
    if not teststr.__getitem__(i).isspace():
        test+=teststr.__getitem__(i)
    i-=1
print(teststr == string)













if not vowel.__contains__(initial):
    temp = str(string)[1:]
    # initial remains
else:
    temp = string[:]
    initial = ""
final_str = temp+'-'+initial+"ay"
print(final_str)


