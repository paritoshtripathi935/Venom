"""
Mr. ABC decided to organise a hackathon for employees one day. He planned to have teams with 3-member squad for the same. In his office. there are N
employees each with different level or ranking i.e. ranks = [1, (2, Is...IN] in programming. ABC found that a balanced team will be formed if it is led by a
single employee whose rank is equal to the sum of the remaining two employee's ranks. Let us help ABC in counting how many such distinct teams are
possible with the given ranks .
return number of teams possible
# constraints
1 <= N <= 100
1 <= ranks[i] <= 100
"""
def hackathonRanks(n, ranks):
    # Write your code here
    ranks.sort()
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            sum = ranks[i] + ranks[j]
            if sum in ranks[j+1:]:
                count += ranks[j+1:].count(sum)
    return count

if __name__ == '__main__':
    n = int(input())
    ranks = list(map(int, input().rstrip().split()))
    result = hackathonRanks(n, ranks)
    print(result)
