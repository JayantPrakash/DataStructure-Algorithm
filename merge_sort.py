def merge_sort(a):
    msort(a, 0, len(a)-1)
    return a
def msort(l, start, end):

    if start >= end:
        return
    
    mid = int((start + end)/2)

    msort(l, start, mid)
    msort(l, mid + 1, end)

    mlist = []
    i = start
    j = mid + 1
    
    while i <= mid and j <=end:
        if l[i] > l[j]:
            mlist.append(l[j])
            j += 1
        else:
            mlist.append(l[i])
            i += 1   

    while i <= mid:
        mlist.append(l[i])
        i+=1

    while j <= end:
        mlist.append(l[j])
        j+=1

    l[start:end+1] = mlist    
    #return l    

print(merge_sort([6,3,8,1,5,2,7]))
