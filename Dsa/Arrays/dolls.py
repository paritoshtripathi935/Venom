

def Dolls(n, arr):
    arr.sort()

    for i in range(0, n-1, 2):
        if arr[i] != arr[i+1]:
            return arr[i]

    return arr[n-1] 
            


def main():
    T = int(input())
    
    for i in range(T):
        N = int(input())
        arr = []
        for i in range(N):
            arr.append(int(input()))
            
        print(Dolls(N, arr))


main()
        