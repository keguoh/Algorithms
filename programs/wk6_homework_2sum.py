"""
Download the following text file:

algo1-programming_prob-2sum.txt

The goal of this problem is to implement a variant of the 2-SUM algorithm 
(covered in the Week 6 lecture on hash table applications).

The file contains 1 million integers, both positive and negative (there might 
be some repetitions!).This is your array of integers, with the ith row of the 
file specifying the ith entry of the array.

Your task is to compute the number of target values t in the interval
[-10000,10000] (inclusive) such that there are distinct numbers x,y in the
input file that satisfy x+y=t. (NOTE: ensuring distinctness requires a 
one-line addition to the algorithm from lecture.)

Write your numeric answer (an integer between 0 and 20001) in the space 
provided.

OPTIONAL CHALLENGE: If this problem is too easy for you, try implementing your 
own hash table for it. For example, you could compare performance under the 
chaining and open addressing approaches to resolving collisions.
"""


# https://github.com/emauton/projects/tree/master/Algorithms

import time


time1 = time.time()

numbers = [int(l) for l in open("wk6_2sum.txt", "r")]
targets = xrange(-10000,10001)
H = {}
answers = {}

for i in numbers:
  H[i] = True

for i in numbers:
  for t in targets:
    if t - i in H:
      if i == t - i:
        continue
      if t not in answers:
        answers[t] = True
        # answers[t] = set([tuple(sorted([i, t - i]))])
      # else:
        # answers[t].add(tuple(sorted([i, t - i])))

print len(answers)


print 'The process takes %s mins' % ((time.time() - time1) / 60)