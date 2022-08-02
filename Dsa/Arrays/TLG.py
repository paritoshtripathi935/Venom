 
def TLG(T):
    diff = 0
    sum1 = 0
    sum2 = 0
    winner = 0 
    lead = 0
    for i in range(T):
        p1, p2 = map(int, input().split(" "))
        sum1 += p1
        sum2 += p2
        if sum1 > sum2:
            diff = sum1 - sum2
            if diff > lead:
                winner = 1
                lead = diff
        elif sum2 > sum1:
            diff = sum2 - sum1
            if diff > lead:
                winner = 2
                lead = diff
    print(winner, lead)



T = int(input())
TLG(T)