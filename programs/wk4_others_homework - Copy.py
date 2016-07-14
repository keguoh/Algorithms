import argparse
import re
from copy import deepcopy
from collections import defaultdict
import sys
import thread
sys.setrecursionlimit(100000)
print thread.stack_size()
thread.stack_size(262144)

class Books:
    def __init__(self):
        self.explored = set()
        self.flag = 1
        self.t = 0
        self.leaderList = defaultdict(list)
        self.leader = 0
        self.finish = []

def DFS(thisGraph, i, book):
    #print 'indfs'
    #print 'i is: ', i
    book.explored.add(int(i))
    book.leaderList[int(book.leader)].append(int(i))
    #print thisGraph
    for arc in thisGraph[i]:
        #print 'looping. book.explored= ', book.explored
        if arc not in book.explored:
            #print book.flag
            #if not book.flag:
                
                #print book.leaderList[arc]
            DFS(thisGraph, arc, book)


    if book.flag:
        book.finish.append(i)

   
    
    
    
    
def DFSLoop(graph, book):
    print 'indfsloop'
    if book.flag:  
        ilist = range(len(graph))
    else:
        ilist = reversed(book.finish)
    book.explored.clear()    
    #book.explored.add(0)
    book.leader = 0
    for i in ilist:
        #print"i: ", i
        if i not in book.explored:

            book.leader = i
            DFS(graph, i, book)
    #print "leaders: ", book.leaderList
    #print "magic nums: ", book.finish
    
            
def GetSCC(graph, revGraph):
    print 'getting SCCs'
    a = Books()
    DFSLoop(revGraph, a)
    a.flag = 0
    a.leaderList.clear()
    DFSLoop(graph, a)
    akey = '0'
    adata = 0
    #for key, data in a.leaderList.items():
        #if len(data) > adata:
            #akey = key
            #adata = len(data)
    print a.leaderList
    #myKey = max(a.leaderList, key=lambda k: len(a.leaderList[k]))
    myAnswer = sorted((len(v) for v in a.leaderList.itervalues()), reverse = True)[:5]
    print 'the biggest SCCs are :', myAnswer
    for item in a.leaderList:
        print item
        print len(a.leaderList[item])
            
def ReadGraph(fileName):
    print 'reading the file'
    graph = defaultdict(list)
    revGraph = defaultdict(list)
    f = open(fileName)
    #graph[0].append(0)
    for line in f:
        line = re.sub('\s\s*', ' ', line)
        v, a = line.split()
        graph[int(v)-1].append(int(a)-1)
        revGraph[int(a)-1].append(int(v)-1)
    print 'finished creating graphs from file'
    #for arc in graph:
        #print arc, ': ', graph[arc]   
    return graph, revGraph
        
def Main():
    parser = argparse.ArgumentParser(description='Calculate largest SCCs in a graph')
    parser.add_argument('-f', dest='fileName', default='.\wk4_SCC.txt')
    args = parser.parse_args()
    graph, revGraph = ReadGraph(args.fileName)
    GetSCC(graph, revGraph)
    
Main()
