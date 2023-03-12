def mergeSort(alist):
    '''
    Divide and conquer strategy
    A recursive algorithm that continually splits in half.
    If the list is empty or has on item, it is sorted by definition(the base case).
    If the list has more than one item, we split the list and recursively invoke a merge sort on both halves.
    Once the two halves are sorted, they are merged.
    '''
    print("Splitting ", alist)
    if len(alist) > 1: # base case (if list is <= 1 then it's already sorted)
        mid = len(alist) // 2 # divide by 2 (left half and right half)
        lefthalf = alist[:mid] # slice the left half until one item
        righthalf = alist[mid:] # slice the right half until one item

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        # sort each half one at a time
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        # sort left half one at a time
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        # sort right half one at a time
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1
        print("Merging ", alist)

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(alist)
print(alist)

'''
Merge sort requires extra space to hold the two halves as they are extracted with the slicing operations.
This additional space can be a critical factor fi the list is large and can make this sort problematic when working on large data sets.
'''