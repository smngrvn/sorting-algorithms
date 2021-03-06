

def binary_search(array, to_find):
    """ Returns the index of the number to find in the sorted array"""

    print("searching for number " + str(to_find) + " in array :" + str(array))

    found = False
    high = len(array)
    searched = len(array)/2
    while(not found):
        print("trying index " + str(searched))

        if array[searched] == to_find:
            # number found
            found = True
            return searched
        else:
            # number to find is lower
            if array[searched] > to_find:
                high = searched
                searched = searched / 2

            else : # number to find is higher
                high = high
                searched = searched + ((high - searched) / 2)


array = [1, 3, 4, 6, 8, 9, 10, 14, 34]
result = binary_search(array, 6)
print("Index = " + str(result))
