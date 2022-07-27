n = int(input())
# subtract N from K
def Fairpass(n):
    for i in range(0,n):
        N,K = map(int,input().split())
        if N >= K:
            print("NO")
        elif K > N:
            print("YES")

Fairpass(n)
