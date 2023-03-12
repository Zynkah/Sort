def selectionSort(alist):
    '''
    Looks for the first largest value as it makes a pass and, after completing the pass, places it in the proper location.
    Repeats this process till all are in the correct order.
    '''
    for fillslot in range(len(alist)-1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            # if the location for the largest number is incorrect, moves it to the correct location.
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location
        
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax]= temp

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selectionSort(alist)
print(alist)

# More efficient and less moves than the bubble sort.