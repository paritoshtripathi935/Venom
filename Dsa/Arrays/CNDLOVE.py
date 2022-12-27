# cook your dish here

def candy_love(N, arr):
    if sum(arr) % 2 ==0:
        print("NO")
    else:
        print("YES")


def main():
    T = int(input())
    
    for i in range(T):
        N = int(input())
        arr = list(map(int, input().split()))
        candy_love(N,arr)
    
if __name__ == '__main__':
    main()