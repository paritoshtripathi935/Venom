# return the lexiographically smallest string after you are given a string s and integer k, you can choose one the first k letters of the string s and append them to the end of the string.


import time

def lexiographically_smallest(s, k):
    s = sorted(s)
    return ''.join(s[:k])

print(lexiographically_smallest('abcd', 2))






