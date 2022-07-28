# cook your dish here
n = int(input())

def hotcold(n):
    for i in range(0,n):
        T = int(input())
        if T > 20:
            print("HOT")
        elif T <= 20:
            print("COLD")

hotcold(n)