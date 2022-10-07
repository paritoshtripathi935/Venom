"""
COOP Basket Problem
Consider a supermarket (COOP) in Stockholm where there are 3 baskets containing the blueberries consisting of the positive integers [α, β, γ] in such a way that the first and the second basket consists of the positive integers which lies in between the range:

0 ≤ β < 2α
0 ≤ γ < 2α

A customer named as Jonas want to compute a third integer δ in such a way that satisfies the two conditions:
Condition A
0 ≤ δ < 2α

Condition B   
The value should be maximum of the following local computation such as:
(β ⊕ δ) x (γ ⊕ δ)

 
Input Format:
T = number of test cases.
The first line consists of three positive integers such as [α, β, γ]
Output Format:
Jonas wants to calculate such an integer δ that satisfy the condition of obtaining the maximum value.

"""

def main():
    # Constraints:
    # 1 ≤ T ≤ 100,
    # 1 ≤ α ≤ 10,
    # 0 ≤ β < 2α
    # 0 ≤ γ < 2α

 
    t = int(input())
    for i in range(t):
        a, b, c = map(int, input().split())

        # satisfy constraints
        if 1 <= t <= 100 and 1 <= a <= 10 and 0 <= b < 2**a and 0 <= c < 2**a: # constraints satisfied
            # compute the maximum value
            print(max(b^c, b^a, c^a)) # xor operation 

    
if __name__ == '__main__':
    main()