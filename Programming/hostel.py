"""
Input: There is only single line that consist of three integers and a real number. 
The first integer n, denotes the number of seconds at which a student may enter in the mess. 
The second integer m, denotes the number of staff members. The third integer d, denotes the amount time (in seconds) to serve the students. 
Lastly, real number p, denotes the probability that a student enters at any given seconds.

Output: Display the single real number that is the expected total waiting time of all the students.
"""

# Sample Input 1
# 3 2 1000 0.5000

# Sample Output 1
# 124.7500000000


# Sample Input 2
# 2 1 5 0.4000

# Sample Output
# 0.64

def main():
    n, m, d, p = map(float, input().split())
    # add constraints
    if n < 1 or n > 1000000:
        return
    if m < 1 or m > 1000000:
        return
    if d < 1 or d > 1000000:
        return
    if p < 0 or p > 1:
        return
    # convert above loop into list comprehension
    if n == 1:
        print(0)
    else:
        if m == 1:
            print((n-1)*d*p)
        else:
            if m == n:
                print((n-1)*d*p)
            else:
                if m < n:
                    print((n-m)*d*p)
                else:
                    print((n-1)*d*p)

if __name__ == "__main__":
    main()