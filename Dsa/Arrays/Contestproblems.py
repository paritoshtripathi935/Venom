# cook your dish here
def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        contests = input().split()
        count_38 = 0
        count_108 = 0
        for j in range(n):
            if contests[j] == "START38":
                count_38 += 1
                
            elif contests[j] == "LTIME108":
                count_108 += 1
        print(count_38, count_108)
        
    

main()