# create a function that sorts an array of integers using the counting sort algorithm with appropiate comments

def countingSort(array):
    # create a new array of length equal to the largest value in the array
    count = [0] * (max(array) + 1)

    # for each value in the array, add 1 to the count array at the index of the value
    # this will give us the number of times each value occurs in the array
    # e.g. if the array is [1,2,3,4,5,6,7,8,9,10], the count array will be [0,1,1,1,1,1,1,1,1,1]
    for i in array:
        count[i] += 1

    # for each value in the count array, add the previous value to the count array
    # this will give the index of the value in the array
    # e.g. if the count array is [1, 2, 3, 4, 5], the index array will be [0, 1, 3, 6, 10]
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # create a new array of length equal to the length of the array
    # for each value in the array, insert the value at the index of the count array
    # decrement the count array by 1

    sortedArray = [0] * len(array)

    # for each value in the array, add the value to the sorted array at the index of the count array at the value - 1
    # then subtract 1 from the count array at the index of the value
    # this will ensure that the value is added to the sorted array at the correct index
    # and the value is removed from the count array at the correct index

    for i in array:
        sortedArray[count[i] - 1] = i
        count[i] -= 1
    return sortedArray


# test the function
array = [10, 5, 2, 3, 9, 8, 7, 1, 6, 4 ]
print(countingSort(array))

# print time complexity of above code 
# O(n)


