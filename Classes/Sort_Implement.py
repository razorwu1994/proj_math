#Contains Merge Sort and Bubble sort
#merge has nlogn BIG O
#While bubble has N^2 BIG O

from random import randint
def bubble(storage):
    sto = list(storage[:])
    l = sto.__len__()
    for c in range(0,l):
        for i in range(0, l-1):
            a= int(sto.__getitem__(i))
            b= int(sto.__getitem__(i+1))
            if a>b:
                sto.__setitem__(i+1,a)
                sto.__setitem__(i,b)

    return sto

def merge(storage):
    sto =list(storage[:])# copy list
    l = sto.__len__()
    temp_sto =[]
    for i in range(0,l):
        temp_sto.append(sto[i:i+1])
    sto =[]
    temp = []
    #top-down split done

    i = 0
    while i < l:
        a=int(temp_sto.__getitem__(i).__getitem__(0))
        b=int(temp_sto.__getitem__(i+1).__getitem__(0))
        if a > b:
            temp.append(list(str(b)+str(a)))
        else:
            temp.append(list(str(a)+str(b)))
        i+=2

    i=0
    while i<int(l/2):
        a=int(temp.__getitem__(i).__getitem__(0))
        b=int(temp.__getitem__(i).__getitem__(1))
        c=int(temp.__getitem__(i+1).__getitem__(0))
        d=int(temp.__getitem__(i+1).__getitem__(1))
        temp_sto = [str(a),str(b),str(c),str(d)]
        temp_sto.sort()
        sto.append(temp_sto)
        i+=2
    temp_sto = []
    temp = []
    i=0
    while i <int(l/4):
        a=int(sto.__getitem__(i).__getitem__(0))
        b=int(sto.__getitem__(i).__getitem__(1))
        c=int(sto.__getitem__(i).__getitem__(2))
        d=int(sto.__getitem__(i).__getitem__(3))
        e = int(sto.__getitem__(i+1).__getitem__(0))
        f = int(sto.__getitem__(i+1).__getitem__(1))
        g = int(sto.__getitem__(i + 1).__getitem__(2))
        h = int(sto.__getitem__(i + 1).__getitem__(3))
        temp_sto = [str(a), str(b), str(c), str(d),str(e),str(f),str(g),str(h)]
        temp_sto.sort()
        temp.append(temp_sto)
        i+=2
    sto = []
    for i in range(0,l):
        sto.append(temp.__getitem__(0).__getitem__(i))
    return sto


#roll for random list
storage = []
for i in range(1,9): #run 8 times
    c = randint(1,8)
    while storage.__contains__(c):
        c = randint(1,8)
    storage.append(c)
print(storage)
#llist = merge(storage)
#
llist = bubble(storage)
print(llist[0:])

