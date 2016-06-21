#https://github.com/danishm/python-sorting-algos/blob/master/sorting.py

def partition(alist):
    pivot = alist[0]
    i, j = 1, 1
    while j < len(alist):
        if alist[j] < pivot:
            #print "exchanging %s at %s with %s at %s" % (alist[j], j, alist[i], i)
            (alist[j], alist[i]) = (alist[i], alist[j])
            i += 1
        j += 1
    (alist[0], alist[i-1]) = (alist[i-1], alist[0])
    #print "pivot is %s and alist[0] is %s" % (pivot, alist[0])
    print alist

alist = [3, 2, 8, 5, 1, 4, 7, 6]
partition(alist)




# def quick_sort(items):
#     """ Implementation of quick sort """
#     if len(items) > 1:
#         pivot_index = len(items) / 2
#         smaller_items = []
#         larger_items = []

#         for i, val in enumerate(items):
#             if i != pivot_index:
#                 if val < items[pivot_index]:
#                     smaller_items.append(val)
#                 else:
#                     larger_items.append(val)

#         quick_sort(smaller_items)
#         quick_sort(larger_items)
#         items[:] = smaller_items + [items[pivot_index]] + larger_items
