"""
The file contains the edges of a directed graph. Vertices are labeled as positive integers from 1 to 875714. Every row indicates an edge, the vertex label in first column is the tail and the vertex label in second column is the head (recall the graph is directed, and the edges are directed from the first column vertex to the second column vertex). So for example, the 11th row looks like : "2 47646". This just means that the vertex with label 2 has an outgoing edge to the vertex with label 47646

Your task is to code up the algorithm from the video lectures for computing strongly connected components (SCCs), and to run this algorithm on the given graph.

Output Format: You should output the sizes of the 5 largest SCCs in the given graph, in decreasing order of sizes, separated by commas (avoid any spaces). So if your algorithm computes the sizes of the five largest SCCs to be 500, 400, 300, 200 and 100, then your answer should be "500,400,300,200,100" (without the quotes). If your algorithm finds less than 5 SCCs, then write 0 for the remaining terms. Thus, if your algorithm computes only 3 SCCs whose sizes are 400, 300, and 100, then your answer should be "400,300,100,0,0" (without the quotes). (Note also that your answer should not have any spaces in it.)

WARNING: This is the most challenging programming assignment of the course. Because of the size of the graph you may have to manage memory carefully. The best way to do this depends on your programming language and environment, and we strongly suggest that you exchange tips for doing this on the discussion forums.
"""


fin=open("wk4_SCC.txt", "r")
# fin=open('wk4_test1.txt', 'r')
# fin=open('wk4_test2.txt', 'r')
# fin=open('wk4_test3.txt', 'r')
# fin=open('wk4_test4.txt', 'r')

n_lines = 0
tail = []
for line in fin:
    n_lines += 1
    a = int(line.split()[0])
    if len(tail) == 0:
    	tail.append(a)
    elif  a > tail[len(tail)-1]:
        tail.append(a)
print n_lines
N = tail[len(tail)-1]
print N

fin.seek(0)

G = {}
#graph with the directions as per the input file
Grev = {}
#graph with the directions reversed
for i in range(1, N+1):
    G[i]=[]
    Grev[i]=[]
for line in fin:
    v1=int(line.split()[0])
    v2=int(line.split()[1])
    G[v1].append(v2)
    Grev[v2].append(v1)
fin.close()

# print G[N]
print 'the Grev is %s\n' % Grev

#global variables to keep record
visited = {}
#whether the node is visited or not
finish = {}
#to keep a record of finishing time of the nodes in the first pass
leader = {}
#to keep record of the leaders of the scc in the 2nd pass


def dfs(G, i):
	global t, s
	stack = []
	f = []
	stack.append(i)
	leader[i] = s
	while(len(stack) > 0):
		u = stack[len(stack)-1]
		if visited[u] == 0:
			leader[u] = s
			visited[u] = 1
			if len(G[u]) == 0:
				t += 1
				finish[u] = t
				stack.pop()
				print 'zero outdegree vertex %s has been reached and its finish is %s' % (u, t)
			else:
				for w in G[u]:
					if visited[w] == 0 and w not in stack:
						stack.append(w)
						print "%s's unvisited neighbor %s has been reached, and stack is %s" % (u, w, stack)
		else:
			t += 1
			finish[u] = t 
			print 'visited %s has been reached and its finish is %s' % (u, t)
			stack.pop()
	visited[i] = 1


# i = 2
# s = i
# t = 0
# dfs(Grev, i)
# print finish
# print leader


def dfs_loop(G):
    global t, s, N
    t = 0 #number of nodes processed so far
    s = 0 #current source vertex
    i = N
    for k in range(1, N+1):
#initially setting all to be none 
        visited[k] = 0
        finish[k] = 0
        leader[k] = 0

    while(i > 0):
        if(visited[i] == 0):
            s = i
            print '\nthe leader is %s' % i
            dfs(G, i)
        i -= 1

#everything set
#finally ready to call the functions with the right graph kind in the corr order
dfs_loop(Grev) 
#THE FIRST LOOP ON REVERSE GRAPH
#done with the second step of the three steps algorithm
# construct new graph
print 'the finish after the first pass is %s\n' % finish
# print 'the leader is %s' % leader
newGraph = {}
for i in range(1, N+1):
    temp=[]
    for x in G[i]: 
        temp.append(finish[x])
#to keep record of the edges of the actual nodes in the correct order
    newGraph[finish[i]] = temp

print 'the newGraph is %s\n' % newGraph

dfs_loop(newGraph) #THE SECOND LOOP 
#done with the third step of the three steps algorithm

print 'the leader is '
    # statistics
lst = sorted(leader.values())
stat = []
pre = 0
for i in range(0, N-1):
    if lst[i] != lst[i+1]:
        stat.append(i+1-pre)
        pre = i+1
stat.append(N-pre)
L = sorted(stat)
L.reverse()
print(L[0:10])