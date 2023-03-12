def shellSort(alist):
    '''
    Sometimes called the 'diminishing increment sort'
    Improves on the insertion sort by breaking the original list into a number of smaller sublists, each of which is sorted using an insertion sort.
    Shell sort uses an increment 'i', sometimes called the gap, to create a sublist by choosing all items that are 'i' items apart.
    '''
    sublistcount = len(alist) // 2
    while sublistcount > 0:

        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)

        print("After increments of size", sublistcount, "This list is", alist)

        # sublistcount is floor division of alist(9), so its starts gap of 4, then cut in half to 2, then cut in half to 1(a standard insertion sort).
        sublistcount = sublistcount // 2

def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):

        currentvalue = alist[i]
        position = i

        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = currentvalue

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shellSort(alist)
print(alist)

# Shell sort cuts out the number of times an insert sort is performed, making the final pass very efficient