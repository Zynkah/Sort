def bubbleSort(alist):
    '''
    Makes multiple passes through alist.
    Compares adjacent items and exchanges those that are out of order.
    Each pass through the list places the next largest value in its proper place.
    In essence, each item 'bubbles' up to the location it belongs.
    '''
    for passnum in range(len(alist) -1, 0, -1):
        # iterate through the list of numbers
        for i in range(passnum):
            # if the number is greater than the one next to, swap places
            if alist[i] > alist[i + 1]:
                # repeat process until all numbers are in order, lowest to highest
                temp = alist[i] # temp storage location, avoids overwritting
                alist[i] = alist[i + 1]
                alist[i + 1] = temp

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubbleSort(alist)
print(alist) # [17, 20, 26, 31, 44, 54, 55, 77, 93]

'''
Often considered the most inefficeint sorting method, since it must exchange itmes before the final location is known. 
These 'wasted' exchange operations are very costly. 
However, because the bubble sort makes passes through the entire unsorted portion of the list, bubble sort can be modified to stop early if it finds that the list has become sorted, this is called a short bubble.
'''