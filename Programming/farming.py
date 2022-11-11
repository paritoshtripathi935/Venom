# array X ofsize N and asked them to plant the trees at the point with cartesian coordinates (Xi, Xj) such that i < j
# keep the minimum length of fencing to achieve this task .
#our task is to help the boys to obtain a value equal to twice the area covered by the fence using the minimum length of fencing.

# Input Format
# The first line of input contains an integer N denoting the number of trees.
# The second line of input contains N space separated integers X1, X2, ..., XN denoting the coordinates of the trees.

# Output Format
# Print the minimum length of fencing required to achieve the task.

# The covered portion is a right-angled triangle with vertices (2,4), (2,1), and (4,1). Area = (1/2)*2*3 = 3.
# Twice of the area covered by fence = 6

def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)

def isInside(x1, y1, x2, y2, x3, y3, x, y):
    A = area(x1, y1, x2, y2, x3, y3)
    A1 = area(x, y, x2, y2, x3, y3)
    A2 = area(x1, y1, x, y, x3, y3)
    A3 = area(x1, y1, x2, y2, x, y)
    return (A == A1 + A2 + A3)

def main():
    N = int(input())
    X = list(map(int, input().split()))
    X.sort()
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                if isInside(X[i], 0, X[j], 0, X[k], 0, (X[i] + X[j]) / 2, 1):
                    ans = max(ans, X[j] - X[i] + X[k] - X[j] + X[k] - X[i])
    print(ans)

if __name__ == '__main__':
    main()
