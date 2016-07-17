
"""
In this programming problem you'll code up Dijkstra's shortest-path algorithm.

Download the following text file:

dijkstraData.txt

The file contains an adjacency list representation of an undirected weighted graph with 200 vertices labeled 1 to 200. Each row consists of the node tuples that are adjacent to that particular vertex along with the length of that edge. For example, the 6th row has 6 as the first entry indicating that this row corresponds to the vertex labeled 6. The next entry of this row "141,8200" indicates that there is an edge between vertex 6 and vertex 141 that has length 8200. The rest of the pairs of this row indicate the other vertices adjacent to vertex 6 and the lengths of the corresponding edges.

Your task is to run Dijkstra's shortest-path algorithm on this graph, using 1 (the first vertex) as the source vertex, and to compute the shortest-path distances between 1 and every other vertex of the graph. If there is no path between a vertex v and vertex 1, we'll define the shortest-path distance between 1 and v to be 1000000.

You should report the shortest-path distances to the following ten vertices, in order: 7,37,59,82,99,115,133,165,188,197. You should encode the distances as a comma-separated string of integers. So if you find that all ten of these vertices except 115 are at distance 1000 away from vertex 1 and 115 is 2000 distance away, then your answer should be 1000,1000,1000,1000,1000,2000,1000,1000,1000,1000. Remember the order of reporting DOES MATTER, and the string should be in the same order in which the above ten vertices are given. The string should not contain any spaces. Please type your answer in the space provided.

IMPLEMENTATION NOTES: This graph is small enough that the straightforward O(mn) time implementation of Dijkstra's algorithm should work fine. OPTIONAL: For those of you seeking an additional challenge, try implementing the heap-based version. Note this requires a heap that supports deletions, and you'll probably need to maintain some kind of mapping between vertices and their positions in the heap.
"""

import time

file = open('wk5_dijkstraData.txt', 'r')
G = {}
for line in file:
	node = int(line.split()[0])
	edge_dis = []
	for edges in line.split()[1:]:
		edge_dis.append({int(edges.split(',')[0]): int(edges.split(',')[1])})
	G[node] = edge_dis


def Dijk(G, s):
	global X, A, B
	X = [s]
	A = {s:0}
	B = {s:[]}
	i = 1
	while len(X) < len(G) and i<203:
		dis_v = {}
		# print 'the X is %s when i = %s' % (X, i)
		for v in X:
			node_w = []
			dis_w = []
			for w in G[v]:
				if w.keys()[0] not in X:
					node_w.append(w.keys()[0])
					dis_w.append(A[v] + w.values()[0])
			if len(dis_w) > 0:
				min_dis_w = min(dis_w)
				dis_v[(v, node_w[dis_w.index(min_dis_w)])] = min_dis_w
		if len(dis_v) > 0:
			w_star = min(dis_v, key=dis_v.get)[1]
			v_star = min(dis_v, key=dis_v.get)[0]
			# print 'the v_star is %s, and w_star is %s when i = %s\n' % (v_star, w_star, i)
			min_dis = dis_v[(v_star, w_star)]
			X.append(w_star)
			A[w_star] = min_dis
			# print 'B before is %s' % B
			B[w_star] = list(B[v_star])
			B[w_star].append(v_star)
			# print 'B after is %s' % B
			i += 1

time1 = time.time()
Dijk(G, 1)


for x in [7,37,59,82,99,115,133,165,188,197]:
	print A[x]
print 'the process takes %s mins' % ((time.time() - time1) / 60)