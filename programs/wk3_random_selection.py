#https://github.com/danishm/python-sorting-algos/blob/master/sorting.py

def rand_seletion(alist, n):
    if len(alist)


def quick_sort(alist):
    if len(alist) < 2: return alist
    else:
        pivot = alist[0]
        i, j = 1, 1
        while j < len(alist):
            if alist[j] < pivot:
                #print "exchanging %s at %s with %s at %s" % (alist[j], j, alist[i], i)
                (alist[j], alist[i]) = (alist[i], alist[j])
                i += 1
            j += 1
        (alist[0], alist[i-1]) = (alist[i-1], alist[0])
        print "getting %s" % alist

        left = alist[:(i-1)]
        quick_sort(left)
        alist[:(i-1)] = left
        
        right = alist[i:]
        quick_sort(right)
        alist[i:] = right
        print "The list becomes %s" % alist


alist = [3, 2, 8, 5, 1, 4, 7, 6]
# alist = [1, 3, 5, 2, 4, 6]
quick_sort(alist)
print alist




