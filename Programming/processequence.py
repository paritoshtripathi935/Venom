# select k processes from both the queues and arrange in such a way that they form the highest combined sequence. 
# But relative order of the processes sequence in respective queue must be reserved. 
# So, your task is to give the highest optimal possible sequence of k processes.
#Sample Input 1:

# 3 2 5
# 5 0 3
# 5 6

# Sample Output 1:
# 5 6 5 0 3 (single space separated)

# START OF THE CODE

import math

def optimal_sequence(arr):
    n = len(arr)
    dp = [0]*n
    dp[0] = arr[0]
    for i in range(1, n):
        dp[i] = max(dp[i-1] + arr[i], arr[i])
    return dp



def main():
    n1 , n2, k = map(int, input().split())
    q1 = list(map(int, input().split()))
    q2 = list(map(int, input().split()))

    print(optimal_sequence(q1) + optimal_sequence(q2))

    

if __name__ == '__main__':
    main()
