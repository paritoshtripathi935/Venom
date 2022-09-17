def main():
    n = 3
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    for i in range(n):
        a[i].append(0)
        for j in range(n):
            if i != j:
                for k in range(1, a[i][0]+1):
                    if a[i][k] not in a[j][1:]: # beacause a[j][0] is the number of destinations
                        a[i][-1] += 1           # a[i][-1] is the number of destinations that none of the other two have gone through
    a.sort(key=lambda x: (x[-1], x[0])) 

    # if destinations are unique then print the number of destinations and the destinations
    if a[0][-1] != a[1][-1]:
        print(a[0][-1], end=" ")
        for i in range(1, a[0][0]+1):
            if a[0][i] not in a[1][1:]:
                print(a[0][i], end=" ")
        print()
    # if destinations are not unique then print the number of destinations and the destinations
    for i in range(n):
        print(i+1, a[i][0], *a[i][1:-1])



if __name__ == '__main__':
    main()
