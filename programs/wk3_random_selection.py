#https://github.com/danishm/python-sorting-algos/blob/master/sorting.py

def rand_seletion(alist, n):
    if len(alist) < n:
        print "the order is out of range!"
    else:
        # if len(alist) < 2: return alist
        # else:
            pivot = alist[0]
            i, j = 1, 1
            while j < len(alist):
                if alist[j] < pivot:
                    #print "exchanging %s at %s with %s at %s" % (alist[j], j, alist[i], i)
                    (alist[j], alist[i]) = (alist[i], alist[j])
                    i += 1
                j += 1
            (alist[0], alist[i-1]) = (alist[i-1], alist[0])
            print "the list becomes %s with pivot %s" % (alist, pivot)
            if i == n: 
                print "the result is %s at position %s" % (alist[i-1], i)
                print alist[i-1]
            elif i < n: 
                print "choose the later part %s with result at %s" % (alist[i:], i)
                rand_seletion(alist[i:], n-i)
            else: 
                print "choose the front part %s" % alist[:(i-1)]
                rand_seletion(alist[:(i-1)], n)



alist = [3, 2, 8, 5, 1, 4, 7, 6]
# alist = [1, 3, 5, 2, 4, 6]
rand_seletion(alist, 7)
print alist


