#http://codereview.stackexchange.com/questions/12922/inversion-count-using-merge-sort

count = 0

def merge_sort(li, c):
    print ('spliting', li)
    if len(li) < 2: return li    #end of the reccursion
    m = len(li) / 2 
    return merge(merge_sort(li[:m], c), merge_sort(li[m:], c), c) 

def merge(l, r, c):
    print "merging %s and %s" % (l ,r)
    result = []
    l.reverse()
    r.reverse() 
    while l and r: 
        s = l if l[-1] < r[-1] else r 
        result.append(s.pop())
        if (s == r): c[0] += len(l)
    print "the count is %s now" % c
    rest = l if l else r
    rest.reverse()
    result.extend(rest)
    return result
    
    
count = [0]
unsorted = [1,5,3,2,4]
print merge_sort(unsorted, count)
print count[0]
