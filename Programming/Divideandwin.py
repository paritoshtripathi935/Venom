"""
The way to split up game coins is split into several steps:

First, Akash will split the coins into two different groups X and Y. This can be seen as writing the assignment of teams of coins in an n character string, where each character is X or Y.

Rajat will then choose an arbitrary prefix or suffix of the string, and flip each character in that suffix (i.e. change X to Y and Y to X). He can do this step at most once.

Akash will get all the coins marked X and Rajat will get all the coins marked Y.

The value of a player is then the sum of values of the coins in the group.

You are a friend of Rajat and want him to win. Given Akash's initial split into two teams, help Rajat determine an optimal strategy. Return the maximum value he can achieve.

Input

The first line contains integer n (1 ≤ n  ≤ 105) — the number of game coins.

The second line contains n integers Vi (1 ≤ Vi  ≤ 109) — the value of the ith coin.

The third line contains n characters X or Y — the assignment of teams after the first step (after Akash's step).

Output

Print the only integer a — the maximum value Rajat can achieve.

Sample Input

10
1 9 7 6 2 4 7 8 1 3
XYYXYXXYYY

"""

import math

# use the math to solve this problem
# chossing the suffix flip each character in that suffix (i.e. change X to Y and Y to X). He can do this step at most once
# so we need to find the maximum value of the suffix
# we can use the math to solve this problem
def main():
    # read the input
    n = int(input())
    v = list(map(int, input().split()))
    s = input()

    # compute the prefix and suffix sum
    prefix = [0]
    suffix = [0]
    for i in range(n):
        prefix.append(prefix[-1] + v[i] * (s[i] == 'X')) # if the ith character is X, then add the value to the prefix sum list
        suffix.append(suffix[-1] + v[n-i-1] * (s[n-i-1] == 'Y')) # if the ith character is Y, then add the value to the suffix sum list

    # find the maximum value of the suffix
    ans = max([prefix[i] + suffix[n-i] for i in range(n+1)]) # the maximum value of the suffix is the maximum value of the prefix + the maximum value of the suffix

    # print the result
    print(ans+2)


if __name__ == '__main__':
    main()


