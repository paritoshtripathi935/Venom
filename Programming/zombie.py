"""
You are in a zombie island where dead zombies want to eat you aliv
zombies, you need to reach at a safe position, say k.

You can only take steps in two ways
1. You can jump to the position which is twice the integer number where you are standing.
2. You can jump to the backward position by one integer.
If at any point, you reach the negative position, zombies will eat you and you are dead.

Complete the function minStepsReq with the following parameters
. First line contains a positive integer n represents the starting position.
. Next line contains a positive integer k represents the destination.

Function should return
An integer represents minimum number of steps required to reach position k.

"""
def minStepsReq(n, k):
    # Write your code here
    if n == k:
        return 0
    elif n > k: # if n is greater than k, then we can only move backwards
        return n - k
    else: # if n is less than k, then we can move forward or backwards
        if k % 2 == 0:
            return 1 + minStepsReq(n, k // 2) # // we use this to get the integer value
        else:
            return 1 + minStepsReq(n, k + 1) # +1 we use this to get the integer value

if __name__ == '__main__':
    n = int(input().strip())
    k = int(input().strip())
    print(minStepsReq(n, k))