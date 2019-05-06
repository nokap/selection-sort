def sortma (inputt): #defining function and placing a singular input, the array
    for iterator1 in range(len(inputt)): #for the first iterator within the range and length of the input...
        min = iterator1 #the minimum value will be the first iterator.
        for iterator2 in range(iterator1,len(inputt)): #for the second iterator within the range of the first iterator and the length of the input...
            if inputt[iterator2] < inputt[min]: #if at the certain point within the input, iterator2 is less than the inputt at its lowest point, then...
                min = iterator2 #the second iterator at that certain point then becomes the minimum
        current = inputt[iterator1] #the current access point is the current point of the first iterator.
        current = inputt[min] #current also is equal to the access point of the second iterator
    return inputt #return the sorted array


print(sortma([7,18,9,32,11,14]))
print(sortma([22,35,3,16,78,91]))
