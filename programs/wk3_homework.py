<<<<<<< HEAD
# Download the following text file:

# kargerMinCut.txt
# The file contains the adjacency list representation of a simple undirected graph. There are 200 vertices labeled 1 to 200. The first column in the file represents the vertex label, and the particular row (other entries except the first column) tells all the vertices that the vertex is adjacent to. So for example, the 6th row looks like : "6  155 56  52  120 ......". This just means that the vertex with label 6 is adjacent to (i.e., shares an edge with) the vertices with labels 155,56,52,120,......,etc
# Your task is to code up and run the randomized contraction algorithm for the min cut problem and use it on the above graph to compute the min cut. (HINT: Note that you'll have to figure out an implementation of edge contractions. Initially, you might want to do this naively, creating a new graph from the old every time there's an edge contraction. But you should also think about more efficient implementations.) (WARNING: As per the video lectures, please make sure to run the algorithm many times with different random seeds, and remember the smallest cut that you ever find.) Write your numeric answer in the space provided. So e.g., if your answer is 5, just type 5 in the space provided.
# https://github.com/smutneja03/Coursera-Algorithms_Part1/blob/master/Week3/karger.py

import random

file = open("wk3_kargerMinCut.txt", "r")
graph = {}
for line in file:
    vertex = int(line.split()[0])
    edges = []
    for edge in line.split()[1:]:
        edges.append(int(edge))
    graph[vertex] = edges
file.close()

def hw3(graph):
    # print "The initial graph is %s" % graph
    while len(graph) > 2:
        start = random.choice(graph.keys())
        # print "start is %s" % start
        end = random.choice(graph[start])
        # print "end is %s" % end
        for node in graph[end]:
            if node != start: 
                graph[start].append(node)
        for node in graph[end]:
            graph[node].remove(end)
            if node != start: 
                graph[node].append(start)
        del graph[end]
        # print "graph becomes %s" % graph

hw3(graph)
print graph
for i in graph:
=======
# Download the following text file:

# kargerMinCut.txt
# The file contains the adjacency list representation of a simple undirected graph. There are 200 vertices labeled 1 to 200. The first column in the file represents the vertex label, and the particular row (other entries except the first column) tells all the vertices that the vertex is adjacent to. So for example, the 6th row looks like : "6  155 56  52  120 ......". This just means that the vertex with label 6 is adjacent to (i.e., shares an edge with) the vertices with labels 155,56,52,120,......,etc
# Your task is to code up and run the randomized contraction algorithm for the min cut problem and use it on the above graph to compute the min cut. (HINT: Note that you'll have to figure out an implementation of edge contractions. Initially, you might want to do this naively, creating a new graph from the old every time there's an edge contraction. But you should also think about more efficient implementations.) (WARNING: As per the video lectures, please make sure to run the algorithm many times with different random seeds, and remember the smallest cut that you ever find.) Write your numeric answer in the space provided. So e.g., if your answer is 5, just type 5 in the space provided.
# https://github.com/smutneja03/Coursera-Algorithms_Part1/blob/master/Week3/karger.py

import random

file = open("wk3_kargerMinCut.txt", "r")
graph = {}
for line in file:
    vertex = int(line.split()[0])
    edges = []
    for edge in line.split()[1:]:
        edges.append(int(edge))
    graph[vertex] = edges
file.close()

def hw3(graph):
    # print "The initial graph is %s" % graph
    while len(graph) > 2:
        start = random.choice(graph.keys())
        # print "start is %s" % start
        end = random.choice(graph[start])
        # print "end is %s" % end
        for node in graph[end]:
            if node != start: 
                graph[start].append(node)
        for node in graph[end]:
            graph[node].remove(end)
            if node != start: 
                graph[node].append(start)
        del graph[end]
        # print "graph becomes %s" % graph

hw3(graph)
print graph
for i in graph:
>>>>>>> 2532d6f9ae5f9c027b6042165f2ee21e71e7c3a8
    print len(graph[i])