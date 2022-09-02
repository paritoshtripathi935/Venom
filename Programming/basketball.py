# You have been appointed as a coach of Bennett Basketball team. Your task is to select players in your team. 
# You believe that short-height student plays better than the tall student.
# All the students are standing in a line, you think a student is short if he/she is shorter than both of his/her neighbours. 

# Find the maximum number of students that you can select in your team. You can reorder the students in a line as you wish.  


def basketball(students):
    # Write your code here
    max_students = 0
    for i in range(len(students)): # loop through the students
        if students[i] < students[i-1] and students[i] < students[i+1]:  # if the student is short and his/her neighbours are taller than him/her
            max_students += 1                                            # add 1 to the max_students count
        if i == 0 or i == len(students)-1:                             # if the student is the first or last student in the line 
            max_students += 1                                            #  add 1 to the max_students count
        
    return max_students


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = basketball(arr)
    print(result)