def insertionSort(alist):
    '''
    Maintains a sorted sublist in the lower positions of the list.
    Each new item is then 'inserted' back into the previous sublist such that the sorted sublist is one item larger.
    '''
    for index in range(1, len(alist)):
        
        currentvalue = alist[index]
        position = index

        # Begins with assuming postion 0 is already sorted
        while position > 0 and alist[position - 1] > currentvalue:
            # On each pass, the item is checked against those sorted in the sublist. Those greater get shifted to the right. 
            alist[position] = alist[position - 1]
            position = position - 1

        # current item inserted when smaller item is reached.
        alist[position] = currentvalue

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertionSort(alist)
print(alist)

'''
O(n^2)
Shift operation requires approximately a third of the provessing work of an exchange since only one assignment is performed.
'''