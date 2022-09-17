f1 = str(input()).split()
for i in range(len(f1)):
    f1[i] = int(f1[i])

f2 = str(input()).split()
for i in range(len(f2)):
    f2[i] = int(f2[i])

f3 = str(input()).split()
for i in range(len(f3)):
    f3[i] = int(f3[i])

f1.pop(0)
f2.pop(0)
f3.pop(0)

dels1 = []
for i in range(len(f1)):
    if f1[i] in f2 or f1[i] in f3:
        dels1.append(i)

dels2 = []
for i in range(len(f2)):
    if f2[i] in f1 or f2[i] in f3:
        dels2.append(i)

dels3 = []
for i in range(len(f3)):
    if f3[i] in f2 or f3[i] in f1:
        dels3.append(i)

if len(dels1) > 1:
    for i in range(len(dels1)):
        f1.pop(dels1[i])
        for j in range(i + 1, len(dels1)):
            dels1[j] -= 1
elif len(dels1) == 1:
    f1.pop(dels1[0])

if len(dels2) > 1:
    for i in range(len(dels2)):
        f2.pop(dels2[i])
        for j in range(i + 1, len(dels2)):
            dels2[j] -= 1
elif len(dels2) == 1:
    f2.pop(dels2[0])

if len(dels3) > 1:
    for i in range(len(dels3)):
        f3.pop(dels3[i])
        for j in range(i + 1, len(dels3)):
            dels3[j] -= 1
elif len(dels3) == 1:
    f3.pop(dels3[0])

places = []
places.append(f1)
places.append(f2)
places.append(f3)

lens = []
lens.append(len(f1))
lens.append(len(f2))
lens.append(len(f3))

maxVal = max(lens)

friends = []
for i in range(len(lens)):
    if lens[i] == maxVal:
        friends.append(i + 1)

for i in friends:
    print(i, end = " ")
    print(lens[i - 1], end = " ")
    if len(places[i-1]) > 1:
        for j in range(len(places[i - 1]) - 1):
            print(places[i - 1][j], end = " ")
        print(places[i - 1][-1])
    else:
        print(places[i - 1][0])