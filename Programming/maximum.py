# Maximum Height Problem
# harry is interested in solving puzzles and games. He has a list of K balls that he must arrange in a triangular shape cupboard such that in the first row only 1 ball can be accommodated, then in the second row only 2 balls can be accommodated, and in the Nth row, there will be maximum N balls in the triangular cupboard as shown in the figure. Consider that the number of rows is equal to the height of the triangle by using the maximum number of balls in each row. Looking at the example, we considered the triangle with height = 5 with 15 balls.

 

# Sample Input:
# N: No. of test cases
# K: Number of balls
# Sample Output:

# Maximum possible height H of the triangle.
# Constraints:
# 1 <= N <= 100
# 1 <= K <= 1000
#Example 1:
#Input:
#3
#3  5  7
#Output:
#2  2  3

# start code here
# import modules
import math
def max_height(k): # function to find the maximum height of the triangle with k balls
    return math.floor((-1 + math.sqrt(1 + 8 * k)) / 2)  # we use math module to find the square root of the equation

def main():
    n = int(input())
    k = list(map(int, input().split()))
    for i in range(n):
        print(max_height(k[i]), end =" ")

if __name__ == "__main__":
    main()

# time complexity: O(n)

    

