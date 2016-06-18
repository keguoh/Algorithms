def inversion_count(alist):
    if len(alist) > 1:
        print 'spliting' + alist
        mid = len(alist)//2
        first_half = alist[:mid]
        second_half = alist[mid:]

        inversion_count(first_half)
        inversion_count(second_half)

        i = 0
        j = 0
        k = 0

        while len(first_half) > i and len(second_half) > j:
            if first_half[i] < second_half[j]:
                alist[k] = first_half[i]
                i++
            else:
                alist[k] = second_half[j]

                

    else:
        print 'reached single-item list'
