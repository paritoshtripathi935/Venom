"""
A disaster situation is depicted with a N x N matrix. The cell of the matrix will contain a doctor (D) or patient (P). A doctor can only treat a patient if both of
them are in same row.
Note

. Each doctor can treat only one patient.
A doctor cannot treat a patient if he is more than X cell away from the doctor.
You have to write a program to find maximum number of patients that can be treated.

Complete the function docPatMatrix with the parameters:
"""

def docPatMatrix(matrix, x, n):
    # save the number of patients that can be treated
    count = 0
    # iterate through the matrix
    for i in range(n):
        # save the index of the doctor
        doc = -1
        # iterate through the row
        for j in range(n):
            # if the cell contains a doctor
            if matrix[i][j] == 'D':
                # save the index of the doctor
                doc = j
            # if the cell contains a patient
            elif matrix[i][j] == 'P':
                # if the doctor is within the range
                if doc != -1 and j - doc <= x:
                    # increment the count
                    count += 1
                    # reset the index of the doctor
                    doc = -1
    # return the number of patients that can be treated
    return count

# Driver code
if __name__ == '__main__':
    n = int(input())
    x = int(input())
    m = input().split(",")
    print(docPatMatrix(m, x, n))