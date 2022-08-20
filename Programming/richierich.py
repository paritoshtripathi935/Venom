# cook your dish here
t = int(input())

def richierich(t):
    for i in range(0,t):
        networth,goal,rate = map(int,input().split())
    
        if networth >= goal:
            print("0")
        elif networth < goal:
            years = int(goal - networth )
            years = int(years / rate)
            print(years)

richierich(t)