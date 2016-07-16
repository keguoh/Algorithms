import time

def dij(G, s):
	X = [s]
	A = {s:0}
	B = {s:[]}
	while len(X) < len(G):

		# how to represent distance of edge?