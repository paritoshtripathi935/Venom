"""
Chef got his dream seat in F1 and secured a 3 rd place in his debut race. He now wants to know the time gap between him and the winner of the race.
You are his chief engineer and you only know the time gap between Chef and the runner up of the race, given as AA seconds, and the time gap between the runner up and the winner of the race, given as BB seconds.
Please calculate and inform Chef about the time gap between him and the winner of the race.

Constraints
1≤T≤100
1≤A,B≤10
"""

def main():
    t = int(input())
    # check for constraints
    if t < 1 or t > 100:
        #print("Constraints not satisfied")
        return
    for i in range(t):
        a, b = map(int, input().split())
        # check for constraints
        if a < 1 or a > 10 or b < 1 or b > 10:
            #print("Constraints not satisfied")
            return
        print(a + b)

if __name__ == "__main__":
    main()
