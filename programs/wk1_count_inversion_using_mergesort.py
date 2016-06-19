"""
This is for programming assignment of week 1
"""

count = 0
def count_inversion_using_mergesort(alist):
    global count
    if len(alist) > 1:
        #print 'spliting %s' % alist
        mid = len(alist)//2
        first_half = alist[:mid]
        second_half = alist[mid:]

        count_inversion_using_mergesort(first_half)
        count_inversion_using_mergesort(second_half)

        i = 0
        j = 0
        k = 0

        while len(first_half) > i and len(second_half) > j:
            if first_half[i] <= second_half[j]:
                alist[k] = first_half[i]
                i = i + 1
            else:
                alist[k] = second_half[j]
                count += len(first_half) - i
                #print "Now we have %s inversions" % count
                j = j + 1
            k = k + 1

        while len(first_half) > i:
            alist[k] = first_half[i]
            i = i + 1
            k = k + 1

        while len(second_half) > j:
            alist[k] = second_half[j]
            j = j + 1
            k = k + 1
        #print (alist, ' merged')
    #else:
        #print 'single-item list %s reached' % alist

#A = [1,3,5,2,4,6]
#A = [1,5,3,2,4]
A = []
Array = open('integerArray.txt')
for i in range(100000):
    A.append(int(Array.readline()))
count_inversion_using_mergesort(A)
print 'the first 20 elements of list become %s and total inversion count is %s' % (A[:20], count)
