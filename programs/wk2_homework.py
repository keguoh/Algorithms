# Problem 1
def quick_sort(alist, count):
    if len(alist) < 2: return alist
    else:
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
        quick_sort(left, count)
        alist[:(i-1)] = left
        right = alist[i:]
        quick_sort(right, count)
        alist[i:] = right
        # print "The list becomes %s" % alist


# alist = [3, 2, 8, 5, 1, 4, 7, 6]
# alist = [1,3,5,2,4,6]

A = open("C:\Users\Keguo\Documents\GitHub\Algorithms\programs\wk2_QuickSort.txt")
alist = []
for i in xrange(10000):
    alist.append(int(A.readline()))
count = [0]
quick_sort(alist, count)
print count
print "\n\n"

# problem 2
def quick_sort_last(alist, count):
    if len(alist) < 2: return alist
    else:
        pivot = alist[-1]
        count[0] += len(alist) - 1
        i, j = -2, -2
        while -j <= len(alist):
            if alist[j] > pivot:
                #print "exchanging %s at %s with %s at %s" % (alist[j], j, alist[i], i)
                (alist[j], alist[i]) = (alist[i], alist[j])
                i -= 1
            j -= 1
        (alist[-1], alist[i+1]) = (alist[i+1], alist[-1])
        # print "the list becomes %s with pivot %s after %s comparisions" % (alist, pivot, count[0])
        left = alist[:(i+1)]
        # print "left is %s" % left
        quick_sort_last(left, count)
        alist[:(i+1)] = left
        if i + 2 < 0:
            right = alist[(i+2):]
            # print "right is %s" % right
            quick_sort_last(right, count)
            alist[(i+2):] = right
        # print "The list becomes %s" % alist


A = open("C:\Users\Keguo\Documents\GitHub\Algorithms\programs\wk2_QuickSort.txt")
alist = []
for i in xrange(10000):
    alist.append(int(A.readline()))
count = [0]
# alist = [3, 2, 8, 5, 1, 4, 7, 6]

# alist = [1,3,5,2,4,6]
# print alist[:20]
# print alist[9990:]
quick_sort_last(alist, count)
print count
# print alist[:20]
# print alist[9990:]
print "\n\n"

# problem 3
def quick_sort_median(alist, count):
    if len(alist) < 2: return alist
    else:
        if len(alist) % 2 == 0:
            pivot_index = len(alist)//2-1
        else: pivot_index = len(alist)//2
        pivot = alist[pivot_index]
        count[0] += len(alist) - 1
        i, j = 0, 0
        a = range(len(alist))
        indx = [s for s in a if s != pivot_index]
        while j in indx:
            if alist[j] < pivot:
                #print "exchanging %s at %s with %s at %s" % (alist[j], j, alist[i], i)
                (alist[j], alist[i]) = (alist[i], alist[j])
                i += 1
            j += 1
        (alist[pivot_index], alist[i-1]) = (alist[i-1], alist[pivot_index])
        print "the list becomes %s with pivot %s after %s comparisions" % (alist, pivot, count[0])
        left = alist[:pivot_index]
        quick_sort_median(left, count)
        alist[:pivot_index] = left
        right = alist[(pivot_index+1):]
        quick_sort_median(right, count)
        alist[(pivot_index+1):] = right
        print "The list becomes %s" % alist

# def p3(alist, count):
# 	first = alist[0]
# 	last = alist[-1]
# 	if len(alist) % 2 == 0:
# 		median = alist[len(alist)//2-1]
# 	else: median = alist[len(alist)//2]


# A = open("C:\Users\Keguo\Documents\GitHub\Algorithms\programs\wk2_QuickSort.txt")
# alist = []
# for i in xrange(10000):
#     alist.append(int(A.readline()))
count = [0]
alist = [3, 2, 8, 5, 1, 4, 7, 6]

# alist = [1,3,5,2,4,6]
# print alist[:20]
# print alist[9990:]
quick_sort_median(alist, count)
print count
print alist[:20]
# print alist[9990:]

