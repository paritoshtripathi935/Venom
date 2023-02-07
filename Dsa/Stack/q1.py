"""
Now, we'll try to solve a famous stack problem.
You are given an array A of size N. You need to push the elements of the array into a stack
and then print minimum in the stack at each pop
Input Format:

The first line of input contains T denoting the number of testcases. T testcases follow.
Each testcase contains two lines of input. The first line of input contains size of array N.
The second line of array contains the elements of array separated by spaces.
Output Format:

For each testcase, in a new line, print the required output.
Your Task:
Since this is a function problem, you don't need to take any input. Just complete the
provided functions_push () and _getMinAtPop().

Constraints:
1<-T <-100
1 <-A <- 10
Examples:
input:
2
6
1 2 3 4 5
7
1 6 43 1 2 0 5

Output:
1 1 1 1 1
0 0 1 1 1 1 1
"""

#User function Template for python3

def _push(arr,n):
    #Your code here
    stack = []
    for i in range(n):
        stack.append(arr[i])
    return stack

def _getMinAtPop(stack,n):
    #Your code here
    min = stack[0]
    for i in range(n):
        if stack[i] < min:
            min = stack[i]

        print(min, end=" ")

    return

if __name__ == "__main__":
	t = int(input())
	while(t>0):
		n = int(input())
		list1 = [int(i) for i in input().strip().split()]
		mys = _push(list1,n)
		_getMinAtPop(mys,n)
		print()
		t = t-1

# } Driver Code Ends