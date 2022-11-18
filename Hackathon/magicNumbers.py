"""
You went to meet a magician. The magician wants to play a game with you which involves money. The magician will write N numbers
which you are not aware of. You can choose any one number out of these numbers randomly. Now the rule is, the rest of the numbers
greater than or equal to your chosen number become equal to your chosen number and all the numbers less than your chosen
number will be multiplied by -1. The magician will pay you the sum of all the modified values. Now, you must find the maximum sum of
all the number after choosing any random number to maximise your chance. Sum of all the numbers over test cases should not
exceed 106
"""
def magicNumbers(arr):
    # Write your code here
    # choose random number

    arr.sort()
    # amke arr set
    arr = list(set(arr))
    max_sum = 0
    for i in range(len(arr)):
        sum = 0
        for j in range(len(arr)):
            if arr[j] >= arr[i]:
                sum += arr[i]
            else:
                sum += -arr[j]
        if sum > max_sum:
            max_sum = sum
    if max_sum < 106:
        return max_sum

if __name__ == '__main__':
    arr = [2,3,1]
    print(magicNumbers(arr))