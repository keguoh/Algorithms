# http://codereview.stackexchange.com/questions/12922/inversion-count-using-merge-sort

count = 0

def merge_sort(li):
    print ('spliting', li)
    if len(li) < 2: return li    #end of the recursion
    m = len(li) / 2 
    return merge(merge_sort(li[:m]), merge_sort(li[m:])) 

def merge(l, r):
    print "merging %s and %s" % (l ,r)
    global count
    result = [] 
    i = j = 0 
    while i < len(l) and j < len(r): 
        if l[i] < r[j]: 
            result.append(l[i])
            i += 1 
        else: 
            result.append(r[j])
            count = count + (len(l) - i)
            j += 1
    result.extend(l[i:]) 
    result.extend(r[j:]) 
    return result

unsorted = [1,5,3,2,4]
print merge_sort(unsorted)
print count
