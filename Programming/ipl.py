"""
Indian Premier League tickets are limited so, the Indian Government gives two random numbers a and b to the Dubai Government. 
Dubai Government wants to give the ticket to all candidates with IDs between a and b ( both inclusive ), 
However, due to coronavirus pandemic time Government can't give tickets to every candidate, Dubai Government decides to give the ticket to candidates having special ID,

"""
# A special ID is not divisible by any number of the form p*p where (p>1).
# So your task is to find the number of candidates getting the tickets.

# Input
"""
1
1 10
"""
# Output
"""
7
"""

# start of code and solve it in o(logn) time complexity using sieve of eratosthenes

def ipl():
    n = int(input())
    if n <=10 or n>=1: # constraints
        for i in range(n):
            a,b = map(int, input().split())
            if a <= 100 and b <= 100: # constraints
                count = 0
                for j in range(a, b+1): # loop for checking the condition that number is not divisible by any number of the form p*p where (p>1)
                    if j >=1:  # constraints
                        for k in range(2,j): # loop for checking the condition that number is not divisible by any number of the form p*p where (p>1)
                            if j % (k*k) == 0: # condition that number is not divisible by any number of the form p*p where (p>1)
                                break
                        else:
                            #print(j)
                            count = count +1 # counting the number of candidates getting the tickets
                print(count, '\n')
            else:
                print("Invalid Input")
    else:
        print("Invalid Input")


ipl()
     
# convert def ipl() to cpp here





