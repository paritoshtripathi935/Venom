"""
You are challenging your friend to play ludo with you. Loser must give a big party. He agrees on
your terms and wants to know who is a ludo king. You have decided to give scores for each game.
Score is distributed like this-

1. When you lose a game, you get 0 score.
2. When you win a game, you get either 1 or 2 score depending on the previous game
.e., if you have won the previous game also you get 2 score, otherwise 1 score.


You have written the results of N games played between you and your friend on a paper. You have
written W or L at the ith place depending upon whether you have won or lost the th game. You
don't want to be called a loser and definitely don't want to give party to your friend. So, you decide
to cheat a little while your friend is not looking at you. 

You change the outcome of at most K games to improvise your score. Now calculate the maximum score you will be able to get after cheating.
Input:
5
2
WLWLL
"""

# Write your code here
def ludoKing(N, K, W):
    score = 0
    # chnage k losses to wins and calculate score
    for i in range(N):
        if K == 0:
            break
        if W[i] == 'L':
            W[i] = 'W'
            K -= 1
            score += 1
            # keep checking for L and chnage if score is maximum
            for j in range(i+1, N):
                

    print(W)
    # calculate score on new W
    for i in range(N):
        if W[i] == 'W':
            if W[i-1] == 'W':
                score += 2
                print(score, 'score')
            else:
                score += 1
            
    return score


if __name__ == '__main__':
    N = 5
    K = 2
    # pass array in w
    W = 'WLWLL'
    # convert string to list
    W = list(W)
    #W = ['L', 'W', 'L', 'W', 'L', 'W']
    print(W)
    
    print(ludoKing(N, K, W))

