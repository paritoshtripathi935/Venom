num = int(input())
l1 = list()
gre = 0
count = num
for i in range(num):
    s = int(input())
    l1.append(s)

l1.sort()

for i in l1:
    ans = count * int(i)
    count = count-1
    if(ans >= gre):
        gre = ans
print(gre)