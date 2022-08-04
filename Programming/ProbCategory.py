T = int(input())
def ProbCategory():
     for i in range(T):
        diff = int(input())
        if diff >= 1 and diff < 100:
            print("Easy")
        if diff >= 100 and diff < 200:
            print("Medium")
        if diff >= 200 and diff <= 300:
            print("Hard")

ProbCategory()