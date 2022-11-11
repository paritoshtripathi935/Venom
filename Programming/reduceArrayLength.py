"""
Problem Statement:
You have been given one integer array X of length n, The task is to reduce the length of this array to length 1 by applying following operations:
You can select an index & such that Xi < Xi+1 and remove either Xe or Xi+1 from the array. After removal remaining array parts are
concatenated.
For e.g., for an array [1 7 2]. You can select * = 1. since Xe < Xx+ 1 (1<7), then remove 7. That makes the array [1 2). Now you can select
k = 1 again, since Xi < Xi+1 (1<2). then remove 1 which makes array left with one element [2]

A string YES if is possible to reduce the array to single element using the above operation, otherwise it should return NO

"""
def reduceArrayLength(X):
    # Write your code here
    if len(X) == 1:
        return 'YES'
    else:
        for i in range(len(X) - 1):
            if X[i] < X[i + 1]: # if the current element is less than the next element then remove the next element
                return reduceArrayLength(X[:i] + X[i + 1:]) # return the result of the recursive call
        return 'NO'

if __name__ == '__main__':
    n = int(input().strip())
    X = list(map(int, input().rstrip().split()))
    print(reduceArrayLength(X))