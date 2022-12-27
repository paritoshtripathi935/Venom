# cook your dish here



def prime_reversal(N, A, B):
    a_ones = 0
    b_ones = 0
    if A == B:
        print("YES")
    else:
        for i in range(N):
            if A[i] == "1":
                a_ones = a_ones + 1
                
            if B[i] == "1":
                b_ones = b_ones +1
    
        if a_ones == b_ones:
            print("YES")
        else:
            print("NO")
        
def main():
    T = int(input())
    
    for i in range(T):
        N = int(input())
        A = str(input())
        B = str(input())
        prime_reversal(N,A,B)
        
main()