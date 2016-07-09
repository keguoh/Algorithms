# Breadth-First-Search and compute the distance

def bfs(graph, s):
    explored[s] = 0
    queue = [s]
    while len(queue) > 0:
        v = queue.pop(0)
        for node in graph[v]:
            if node not in explored:
                explored[node] = explored[v] + 1
                queue.append(node)
    print "The explored nodes with its distance to %s are:" % s
    for i in explored:
        print (i, explored[i])


file = open("wk3_test1.txt", "r")
graph = {}
for line in file:
    vertex = int(line.split()[0])
    edges = []
    for edge in line.split()[1:]:
        edges.append(int(edge))
    graph[vertex] = edges
file.close()

explored = {}
print "The original graph is %s\n" % graph
bfs(graph, 3)


# Compute connected components
def connect_comp(graph):
    cc = 0
    for i in range(len(graph)):
        if i+1 not in explored.keys():
            bfs(graph, i+1)
            cc += 1
    print cc

graph = {1:[3,5], 2:[4], 3:[1,5], 4:[2], 5:[1,3,7,9], 6:[8,10], 7:[5], 8:[6,10], 9:[5], 10:[6,8]}

explored={}
connect_comp(graph)