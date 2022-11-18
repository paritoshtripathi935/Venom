"""
In a line, if there are
more than X boys standing one after another successively, or there are more than Y girls standing one after another, then
they start talking and disturb the whole assembly. You need to find out the number of ways you can arrange them in a line so
that not more than X boys or Y girls stand after one another successively.
"""


def countWays(X, Y, N):
    # Write your code here
    if X == 0:
        return 1
    if Y == 0:
        return 1
    if N == 0:
        return 0
    return countWays(X - 1, Y, N - 1) + countWays(X, Y - 1, N - 1)


if __name__ == '__main__':
    X = int(input().strip())

    Y = int(input().strip())

    N = int(input().strip())

    result = countWays(X, Y, N)
    print(result)