"""
You are given a matrix Mat of m rows and n columns. The matrix is boolean so the
elements of the matrix can only be either 0 or 1.
Now, if any row of the matrix contains a 1, then you need to fill that whole row with 1.
After doing the mentioned operation, you need to print the modified matrix.

Input:
The first line of input contains T denoting the number of testcases. T testcases follow.
The first line of each testcase contains m and n denoting number of rows and number of
columns.
Then next m lines contain n elements denoting the elements of the matrix.

Output:
For each testcase, in a new line, print the modified matrix.

Input:
2
54
1000
0000
0100
0000
0001
12
00

Output:
1111
0000
1111
0000
1111
00
"""

def modify_matrix(mat, m, n):
    for i in range(m):
        if 1 in mat[i]:
            mat[i] = [1] * n
    return mat

def binary_matrix(mat, m, n):
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 1:
                for k in range(n):
                    mat[i][k] = 1
                for k in range(m):
                    mat[k][j] = 1
    return mat
    
def main():
    T = int(input())
    for _ in range(T):
        m, n = map(int, input().split())
        mat = []
        for _ in range(m):
            mat.append(list(map(int, input().split())))
        modified_mat = modify_matrix(mat, m, n)
        for row in modified_mat:
            print(' '.join(map(str, row)))
    
if __name__ == '__main__':
    main()
