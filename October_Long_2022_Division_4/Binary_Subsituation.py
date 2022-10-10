def solve():
    s = str(input())
    n = len(s)
    is_different = [0]*n
    for i in range(1,n):
        is_different[i] = 1 if s[i] != s[i-1] else 0
    dp = [[0,0] for _ in range(n)]
    dp[0][0] = 1
    for i in range(1,n):
        dp[i][0] = (dp[i-1][0] + dp[i-1][1])%998244353
        if is_different[i] == 1:
            dp[i][1] = dp[i-1][0]
        else:
            dp[i][1] = 0
    print((dp[n-1][0] + dp[n-1][1])%998244353)


def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()