# take int numbers as input and store in list
n = input().split(" ")
n = list(map(int, n))
count = 0
for i in n:
    if i >= 10:
        count += 1
    else:
        count += 0

print(count)
