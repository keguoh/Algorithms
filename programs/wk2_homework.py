import statistics as st
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
for i in xrange(1000):
    alist.append(int(A.readline()))
A.close()
count = [0]
quick_sort_first(alist, count)
print count
print alist[:20]
print "\n\n"



# problem 2
def quick_sort_last(alist, count):
    if len(alist) >= 2:
        pivot = alist[-1]
        count[0] += len(alist) - 1
        i, j = 0, 0
        while j < len(alist) - 1:
            if alist[j] < pivot:
                #print "exchanging %s at %s with %s at %s" % (alist[j], j, alist[i], i)
                (alist[j], alist[i]) = (alist[i], alist[j])
                i += 1
            j += 1
        (alist[-1], alist[i]) = (alist[i], alist[-1])
        # print "the list becomes %s with pivot %s after %s comparisions" % (alist, pivot, count[0])
        left = alist[:i]
        quick_sort_last(left, count)
        alist[:i] = left
        right = alist[(i+1):]
        quick_sort_last(right, count)
        alist[(i+1):] = right
        # print "The list becomes %s" % alist
# A = open("wk2_QuickSort.txt")
A = open("wk2_test1000.txt")
alist = []
for i in xrange(1000):
    alist.append(int(A.readline()))
A.close()

count = [0]
quick_sort_last(alist, count)
print count
print alist[:20]
print "\n\n"

# Another way
# def quick_sort_last2(alist, count):
#     if len(alist) < 2: return alist
#     else:
#         pivot = alist[-1]
#         count[0] += len(alist) - 1
#         i, j = -2, -2
#         while -j <= len(alist):
#             if alist[j] > pivot:
#                 #print "exchanging %s at %s with %s at %s" % (alist[j], j, alist[i], i)
#                 (alist[j], alist[i]) = (alist[i], alist[j])
#                 i -= 1
#             j -= 1
#         (alist[-1], alist[i+1]) = (alist[i+1], alist[-1])
#         print "the list becomes %s with pivot %s after %s comparisions" % (alist, pivot, count[0])
#         left = alist[:(i+1)]
#         # print "left is %s" % left
#         quick_sort_last2(left, count)
#         alist[:(i+1)] = left
#         if i + 2 < 0:
#             right = alist[(i+2):]
#             # print "right is %s" % right
#             quick_sort_last2(right, count)
#             alist[(i+2):] = right
#         # print "The list becomes %s" % alist



# problem 3
def quick_sort_median(alist, count):
    if len(alist) >= 2:
        if len(alist) % 2 == 0:
            pivot_index = len(alist)//2-1
        else: pivot_index = len(alist)//2
        (alist[pivot_index], alist[0]) = (alist[0], alist[pivot_index])
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
        # print "The list becomes %s" % alist


def partition_first(alist, count):
    i, j = 1, 1
    if len(alist) >= 2:
        pivot = alist[0]
        count[0] += len(alist) - 1
        while j < len(alist):
            if alist[j] < pivot:
                #print "exchanging %s at %s with %s at %s" % (alist[j], j, alist[i], i)
                (alist[j], alist[i]) = (alist[i], alist[j])
                i += 1
            j += 1
        (alist[0], alist[i-1]) = (alist[i-1], alist[0])
        # print pivot_index
    return (i-1)

def partition_median(alist, count):
    i, j = 1, 1
    if len(alist) >= 2:
        if len(alist) % 2 == 0:
            pivot_index = len(alist)//2-1
        else: pivot_index = len(alist)//2
        (alist[pivot_index], alist[0]) = (alist[0], alist[pivot_index])
        pivot = alist[0]
        count[0] += len(alist) - 1
        while j < len(alist):
            if alist[j] < pivot:
                #print "exchanging %s at %s with %s at %s" % (alist[j], j, alist[i], i)
                (alist[j], alist[i]) = (alist[i], alist[j])
                i += 1
            j += 1
        (alist[0], alist[i-1]) = (alist[i-1], alist[0])
        # print pivot_index
    return (i - 1)

def partition_last(alist, count):
    i, j = 0, 0
    if len(alist) >= 2:
        pivot = alist[-1]
        count[0] += len(alist) - 1
        while j < len(alist) - 1:
            if alist[j] < pivot:
                #print "exchanging %s at %s with %s at %s" % (alist[j], j, alist[i], i)
                (alist[j], alist[i]) = (alist[i], alist[j])
                i += 1
            j += 1
        (alist[-1], alist[i]) = (alist[i], alist[-1])
        # print pivot_index
    return i

def quick_sort_p3(alist, count):
	first = alist[0]
	last = alist[-1]
	if len(alist) % 2 == 0:
		median = alist[len(alist)//2-1]
	else: median = alist[len(alist)//2]
	m = st.median([first, median, last])
	# print "choose pivot %s" % m
	if first == m:
		indx = partition_first(alist, count)
	if last == m:
		indx = partition_last(alist, count)
	if median == m and len(alist) > 2:
		indx = partition_median(alist, count)
	# print "the list becomes %s with pivot %s after %s comparisions" % (alist, alist[indx], count[0])

	if indx > 0:
		left = alist[:indx]
		quick_sort_p3(left, count)
		alist[:indx] = left
	if indx + 1 < len(alist):
		right = alist[(indx+1):]
		# print "right is %s" % right
		quick_sort_p3(right, count)
		alist[(indx+1):] = right

# A = open("wk2_QuickSort.txt")
A = open("wk2_test1000.txt")
alist = []
for i in xrange(1000):
    alist.append(int(A.readline()))
A.close()
count = [0]
# alist = [3, 2, 8, 5, 1, 4, 7, 6]
# alist = [1,3,5,2,4,6]
# print alist[:20]
# print alist[9990:]
quick_sort_p3(alist, count)
print count
print alist[:20]

