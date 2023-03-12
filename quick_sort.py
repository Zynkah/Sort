def quickSort(alist):
    '''
    Divide and conquer strategy
    Same advantages as the merge sort, while not using additional storage.
    As a trade-off, it is possible that the list may not be divided in half. When this happens we will see that the performance is diminished.
    '''
    quickSortHelper(alist, 0, len(alist) - 1)

def quickSortHelper(alist, first, last):
    if first < last:

        splitpoint = partition(alist, first, last) # actual position where the pivot value belongs in the final sorted list, used to divide the list for subsequent calls to the quick sort.

        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)

def partition(alist, first, last):
    pivotvalue = alist[first] # first value selected, assists with splitting the list

    # partitionng begines by locating 2 position markers, we will call them left/rigth mark. 
    leftmark = first + 1
    rightmark = last

    done = False
    while not done:
        # The goal of the partition process it to move items that are on the wrong side with respect to the pivot value while also converging on the split point.
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quickSort(alist)
print(alist)

'''
O(n log n) may degrade to O(n^2) if split points are not near the middle of the list
Worst case the split point may not be in the middle and can be very skewed to the left of right, leaving an very uneven division.
To alleviate some of the potential for an uneven division we can use a technique called median of three.
To choose the pivot value, we will consider the first, the middle, and the last of the list.
The idea is that in the case where the first item in the list does not belong toward the middle of the list, the median of three will choose a better 'middle' value. 
'''