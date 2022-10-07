"""
Each pizza consists of 4 slices. There are N friends and each friend needs exactly X slices.
Find the minimum number of pizzas they should order to satisfy their appetite.
1≤T≤100
1≤N,X≤10
"""
def main():
    t = int(input())
    # check for constraints
    if t < 1 or t > 100:
        #print("Constraints not satisfied")
        return
    for i in range(t):
        n, x = map(int, input().split())
        # check for constraints
        if n < 1 or n > 10 or x < 1 or x > 10:
            #print("Constraints not satisfied")
            return
        print((n * x + 3) // 4)
        
if __name__ == "__main__":
    main()