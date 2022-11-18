"""
MS. ABC has N number of bunnies in her house. All the N bunnies have eaten some number of carrots for their dinner C = [C1,C2.C3.....CN]- Now ABC ha
to make su
Note: MS. ABC can feed bunnies with some carrots and make X number of bunnies having same number of carrots. You are requested
to find the minimum number of carrots M she can feed to her bunnies to make X number of bunnies feeded equally.
"""

def minNoOfCarrots(n, x, noOfCarrots):
    # Write your code here
    # max of noOfCarrots
    min =  max(noOfCarrots)
    mini = 0
    # sort
    noOfCarrots.sort()
    # find min
    for i in range(0, len(noOfCarrots)-x+1):
        diff = noOfCarrots[i+x-1] - noOfCarrots[i]
        if diff < min:
            min = diff
            mini = i
    
    sum = 0
    maxval = noOfCarrots[mini+x-1]
    for i in range(mini, mini+x-1):
        sum += (maxval - noOfCarrots[i])
    
    return sum



if __name__ == '__main__':
    n = int(input())
    x = int(input())
    noOfCarrots = list(map(int, input().rstrip().split()))
    result = minNoOfCarrots(n, x, noOfCarrots)
    print(result)
