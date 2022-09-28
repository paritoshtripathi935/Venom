"""
A child is playing a game in which he must collect coins from each store and return to the first store from where he began the collection. 
The shops are set up in a circle. The child initially had two pieces of information, about each store 1. How many coins the store will offer the kid and 2. 
How many steps required to reach to the next store to collect the coins. One requirement is that the child spend one coin at each step. The coin bag is initially empty.

Input Format:
The value of X will be on the first line.
The quantity of coin that store will give and the step between that store and the next store are each represented by a pair of integers in the next X lines.

Output Format:
An integer that will represent the store's lowest starting index for the game.

Sample Input 2

5
1 3
2 4
3 5
4 1
5 2

Sample Output
3

Constraints:

1<=X<=100000
1<=Number of coins,
steps<=1000000000

"""


def main():
    n = int(input())
    coin = []
    step = []

    for i in range(n):
        c, s = map(int, input().split())
        coin.append(c)
        step.append(s)
    # add constraints
    if n < 1 or n > 100000:
        return
    for i in range(n):
        if coin[i] < 1 or coin[i] > 1000000000 or step[i] < 1 or step[i] > 1000000000:
            return
    
    
    # conver above loop into list comprehensio
    for i in range(n):
        if i == 0:
            if coin[i] >= step[i]: # if the first store has enough coins to reach the next store
                print(i)           # then print the index of the first store as the answer
                break
        else:
            if coin[i] >= step[i] + coin[i-1]: # if the store has enough coins to reach the next store and the previous store has enough coins to reach the current store
                print(i)                       # then the current store is the starting point of the game 
                break
            else: 
                if i == n-1: # if the loop reaches the last store and the game is not started from the first store
                    print(0)  # then the game is started from the first store
     # if the loop ends without printing anything, then the first store is the answer
    else:
        print(0)

if __name__ == "__main__":
    main()
