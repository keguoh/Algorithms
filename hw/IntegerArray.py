def inversion_count(alist, count):
    if len(alist) > 1:
        #print 'spliting %s' % alist
        mid = len(alist)//2
        first_half = alist[:mid]
        second_half = alist[mid:]

        inversion_count(first_half, count)
        inversion_count(second_half, count)

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
                print "Now we have %s inversions" % count
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
        print (alist, ' merged')
    #else:
        #print 'single-item list %s reached' % alist

#A = [1,3,5,2,4,6]
A = [1,5,3,2,4]
print A
count = 0
inversion_count(A, count)
print 'list becomes %s and count is %s' % (A, count)
