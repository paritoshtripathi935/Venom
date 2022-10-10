def SOP_ONE(n,s):
    for i in range(n):
        if s[i] == '0':
            return i
    return n

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = str(input())
        print(SOP_ONE(n,s))
    

if __name__ == "__main__":
    main()

