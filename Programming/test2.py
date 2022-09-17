"""
a: Friend Number 
b: No. of travelling destinations that none of the other two have gone through
c: space separated sorted list of b travelling destinations'

Sample Input 1:
2 100 600
2 200 500
2 300 400

Sample Output 1:
1 2 100 600
2 2 200 500
3 2 300 400

"""

#Explanation
#Friend 1 has travelled 2 destinations that none other 2 have with numbers 100 and 600. Friend 2 has travelled 2 destinations that none other 2 have with numbers 200 and 500. Friend 3 has travelled 2 destinations that none other 2 have with numbers 300 and 400.
#So, there is tie between all three. Print in sorted friend number, with no. of such destinations travelled with sorted list.

# take inspiration from test-2.py
# and write your code here

def solve():
    f1 = list(map(int, input().split()))
    f2 = list(map(int, input().split()))
    f3 = list(map(int, input().split()))
    f1.pop(0)
    f2.pop(0)
    f3.pop(0)
    places = [f1, f2, f3]
    ans = []
    for i in range(len(places)):
        count = 0
        for j in range(len(places)):
            if i == j:
                continue
            for k in places[i]:
                if k not in places[j]:
                    count += 1
        ans.append([i + 1, count, sorted(places[i])])
    ans.sort(key=lambda x: (x[1], x[0]))
    for i in ans:
        print(*i)

if __name__ == "__main__":
    solve()
    
