class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def sorted(self,stack):
        #code here
        temp = []
        while stack:
            temp.append(stack.pop())
        while temp:
            curr = temp.pop()
            while stack and stack[-1] > curr:
                temp.append(stack.pop())
            stack.append(curr)
        return stack
    

#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.sorted(arr)
        for e in range(len(arr)):
            print(arr.pop(), end=" ")
        print()


# } Driver Code Ends