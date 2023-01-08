"""
Accuracy: 28.57% Submissions: 14 Points: 100
Given an array arr [] of N positive integers. The task is to find a subsequence with

maximum sum such that there should be no adjacent elements from the array in the
subsequence.
Input:
First line of input contains number of testcases T. For each testcase, first line of input
contains size of array N. Next line contains N elements of the array space seperated.

Output:
For each testcase, print the maximum sum of the subsequence.
Constraints:

Input:
2
3
1 2 3
3
1 20 3
Output:
4
20

Explanation:
Testcase 1: Elements 1 and 3 form a subsequence with maximum sum and no elements
in the subsequence are adjacent in the array.
Testcase 2: Element 20 from the array forms a subsequence with maximum sum.
"""

def max_sum_subsequence(arr):
    n = len(arr)
    if n == 0:
        return 0
    elif n == 1:
        return arr[0]
    elif n == 2:
        return max(arr[0], arr[1])
    else:
        dp = [0] * n
        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])
        for i in range(2, n):
            dp[i] = max(arr[i] + dp[i-2], dp[i-1])
        return dp[n-1]

def main():
    T = int(input())
    for i in range(T):
        n = int(input())
        arr = list(map(int, input().split()))
        print(max_sum_subsequence(arr))

if __name__ == '__main__':
    main()
    