# Eulerian Path - Create a program which will take as an input a graph and output
# either a Eulerian path or a Eulerian cycle, or state that it is not possible.
# A Eulerian Path starts at one node and traverses every edge of a graph
# through every node and finishes at another node.
# A Eulerian cycle is a eulerian Path that starts and finishes at the same node.

from Graphs import Graph_links as GL
from random import randint
import time
#get graph, generates all the links, and start from a vertex with odd num of links
def single_path(start,end):
    return [start,end]
def get_startpoint(len):
    return randint(1, len)
def eu_return(graph):
    temp = {}
    temp.__init__(graph)
    print(temp)
    temp_list =[]
    #generating links
    for i in range(1,temp.__len__()+1):
        for j in range(0,list(temp.get(i)).__len__()):
            temp_list.append([i,list(temp.get(i)).__getitem__(j)])

    print(temp_list)

    path =[]
    links =[]
    startpoint = get_startpoint(temp.__len__())
    path.append(startpoint)
    b_t =[]
    while True:
        endpoint = list(temp.get(startpoint)).__getitem__(randint(0,list(temp.get(startpoint)).__len__()-1))

        if links.__contains__(single_path(startpoint,endpoint)):
            if b_t == single_path(startpoint, endpoint):
                #need to pick new startpoint
                startpoint = get_startpoint(temp.__len__())
                path = []
                links = []
                path.append(startpoint)
                b_t = []

            else:
                b_t = single_path(startpoint, endpoint)
            continue

        path.append(endpoint)

        links.append(single_path(startpoint,endpoint))
        links.append(single_path(endpoint,startpoint))

        startpoint = endpoint

        if path.__len__()==temp.__len__()+1:
            print(path)
            break
    if path.__getitem__(0) == path.__getitem__(path.__len__()-1):
        print("Eu cycle")
    else:
        print("Eu path")


    # startpoint = -1
    #
    # for i in range(1,temp.__len__()+1):
    #     print(temp.__getitem__(i))
    #     if  (list(temp.__getitem__(i)).__len__()% 2) == 1:# means this vertex has odd links
    #         startpoint = i
    #         break
    #
    # assert startpoint > 0
    # print(startpoint)
    #
    # path =[]
    # list(temp.__getitem__(startpoint)).__getitem__()






def is_connect(graph):
    temp={}
    temp.__init__(graph)
    flag = True
    for i in range (1,temp.__len__()+1):
        if list(temp.__getitem__(i)).__contains__(i):
            flag = False
            break
    return flag

graph = GL.fromLinks([(1, 2), (1, 6), (2, 3), (3, 4),(4,5),(5,6),(6,7)])
print(is_connect(graph))
eu_return(graph)