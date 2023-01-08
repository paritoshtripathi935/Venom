"""
A restaurant has n ice creams. Each ice cream has some flavour represented by a;
at least k inidices apart from each other.
Find the number of different ways they can order the ice creams .
Example 1:

Input :
n = 5 , K
a = (1, 2, 2, 1, 2 }
Output :
3

Explanation:
1 3) where distance, 3-0 32 2
where distance, 3-0 >= 2
" where distance , 4-2 >= 2
"""
import math

def count_ice_creams(n, k, a):
    if k == 0:
        return 0
    indices = {}
    for i in range(n):
        if a[i] not in indices:
            indices[a[i]] = [i]
        else:
            indices[a[i]].append(i)
    count = 0
    for flavour, inds in indices.items():
        for i in range(len(inds)):
            for j in range(i+1, len(inds)):
                if inds[j] - inds[i] >= k:
                    count += 1
    if count == 0 and k == 1:
        return 0
    return count


def main():
    n = int(input())
    k = int(input())
    a = list(map(int, input().split()))
    print(count_ice_creams(n, k, a))

if __name__ == '__main__':
    main()