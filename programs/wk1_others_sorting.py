#https://github.com/danishm/python-sorting-algos/blob/master/sorting.py
""" Basic Sorting Algorithms Implemented in Python """

import random
import heapq

def bubble_sort(items):
    """ Implementation of bubble sort """
    for i in range(len(items)):
        for j in range(len(items)-1-i):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]     # Swap!


def insertion_sort(items):
    """ Implementation of insertion sort """
    for i in range(1, len(items)):
        j = i
        while j > 0 and items[j] < items[j-1]:
            items[j], items[j-1] = items[j-1], items[j]
            j -= 1


def merge_sort(items):
    """ Implementation of mergesort """
    if len(items) > 1:

        mid = len(items) / 2        # Determine the midpoint and split
        left = items[0:mid]
        right = items[mid:]

        merge_sort(left)            # Sort left list in-place
        merge_sort(right)           # Sort right list in-place

        l, r = 0, 0
        for i in range(len(items)):     # Merging the left and right list

            lval = left[l] if l < len(left) else None
            rval = right[r] if r < len(right) else None

            if (lval and rval and lval < rval) or rval is None:
                items[i] = lval
                l += 1
            elif (lval and rval and lval >= rval) or lval is None:
                items[i] = rval
                r += 1
            else:
                raise Exception('Could not merge, sub arrays sizes do not match the main array')



def heap_sort(items):
    """ Implementation of heap sort """
    heapq.heapify(items)
    items[:] = [heapq.heappop(items) for i in range(len(items))]
    


if __name__ == '__main__':
    random_items = [random.randint(-50, 100) for c in range(32)]

    print 'Before: ', random_items
    insertion_sort(random_items)        # Replace the funtion name here to
                                        # try any of the other algorithms
    print 'After : ', random_items