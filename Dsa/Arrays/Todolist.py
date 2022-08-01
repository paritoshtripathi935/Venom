def todo():
    N = int(input())
    diff = input().split(" ")
    diff = list(map(int, diff))
    
    count = 0
    for i in range(0,N):
        if diff[i] >= 1000:
            count = count + 1
                
    print(count)    

T = int(input())
while(T > 0):
    T = T - 1
    todo()