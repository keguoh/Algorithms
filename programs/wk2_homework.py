import statistics as st
"""
This is a program which implements the quicksort algorithm
in three different ways.  The first takes the pivot element 
to always be the first element of the array, while the second 
takes the pivot to always be the last element.  The third
way is to consider the first, last, and middle element of
the array and letting the pivot be the median of the three.
This saves time in arrays that are nearly sorted or nearly 
reverse sorted.  This program also calculates the number of
comparisons quicksort uses while sorting.
"""
# Problem 1

def quick_sort_first(alist, count):
    if len(alist) >= 2:
        pivot = alist[0]
        count[0] += len(alist) - 1
        i, j = 1, 1
        while j < len(alist):
            if alist[j] < pivot:
                #print "exchanging %s at %s with %s at %s" % (alist[j], j, alist[i], i)
                (alist[j], alist[i]) = (alist[i], alist[j])
                i += 1
            j += 1
        (alist[0], alist[i-1]) = (alist[i-1], alist[0])
        # print "the list becomes %s with pivot %s after %s comparisions" % (alist, pivot, count[0])
        left = alist[:(i-1)]
        quick_sort_first(left, count)
        alist[:(i-1)] = left
        right = alist[i:]
        quick_sort_first(right, count)
        alist[i:] = right
        # print "The list becomes %s" % alist

# A = open("wk2_QuickSort.txt")
A = open("wk2_test1000.txt")
alist = []
for line in A:
    alist.append(int(line))
A.close()
count = [0]
quick_sort_first(alist, count)
print count
print alist[:20]
print "\n\n"



# problem 2
def quick_sort_last(alist, count):
    if len(alist) >= 2:
        (alist[0], alist[-1]) = (alist[-1], alist[0])
        pivot = alist[0]
        count[0] += len(alist) - 1
        i, j = 1, 1
        while j < len(alist):
            if alist[j] < pivot:
                #print "exchanging %s at %s with %s at %s" % (alist[j], j, alist[i], i)
                (alist[j], alist[i]) = (alist[i], alist[j])
                i += 1
            j += 1
        (alist[0], alist[i-1]) = (alist[i-1], alist[0])
        # print "the list becomes %s with pivot %s after %s comparisions" % (alist, pivot, count[0])
        left = alist[:(i-1)]
        quick_sort_last(left, count)
        alist[:(i-1)] = left
        right = alist[i:]
        quick_sort_last(right, count)
        alist[i:] = right
        # print "The list becomes %s" % alist
# A = open("wk2_QuickSort.txt")
A = open("wk2_test1000.txt")
alist = []
for line in A:
    alist.append(int(line))
A.close()

count = [0]
quick_sort_last(alist, count)
print count
print alist[:20]
print "\n\n"


# problem 3

def med(a, b, c):
    if ( a - b) * (c - a) >= 0:
        return a
    elif (b - a) * (c - b) >= 0:
        return b
    else:
        return c

def quick_sort_median(alist, count):
    if len(alist) >= 2:
        first = alist[0]
        last = alist[-1]
        if len(alist) % 2 == 0:
            median = alist[len(alist)//2-1]
        else: median = alist[len(alist)//2]
        m = med(first, median, last)
        # print "choose pivot %s" % m
        if last == m:
            (alist[0], alist[-1]) = (alist[-1], alist[0])
        if median == m:
            if len(alist) % 2 == 0:
                (alist[len(alist)//2-1], alist[0]) = (alist[0], alist[len(alist)//2-1])
            else: (alist[len(alist)//2], alist[0]) = (alist[0], alist[len(alist)//2])
        # print "the list becomes %s with pivot %s after %s comparisions" % (alist, alist[indx], count[0])
        pivot = alist[0]
        count[0] += len(alist) - 1
        i, j = 1, 1
        while j < len(alist):
            if alist[j] < pivot:
                #print "exchanging %s at %s with %s at %s" % (alist[j], j, alist[i], i)
                (alist[j], alist[i]) = (alist[i], alist[j])
                i += 1
            j += 1
        (alist[0], alist[i-1]) = (alist[i-1], alist[0])
        # print "the list becomes %s with pivot %s after %s comparisions" % (alist, pivot, count[0])
        left = alist[:(i-1)]
        quick_sort_median(left, count)
        alist[:(i-1)] = left
        right = alist[i:]
        quick_sort_median(right, count)
        alist[i:] = right

# A = open("wk2_QuickSort.txt")
A = open("wk2_test1000.txt")
alist = []
for line in A:
    alist.append(int(line))
A.close()
count = [0]
# alist = [3, 2, 8, 5, 1, 4, 7, 6]
# alist = [1,3,5,2,4,6]

# print alist[9990:]
quick_sort_median(alist, count)
print count
print alist[:20]

