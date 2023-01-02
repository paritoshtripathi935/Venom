class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self,A,N,X):
        arr = A
        n = N
        x = X
        #Your code here
        if x < arr[0]:
            return -1
            
        if x >= arr[n-1]:
            return n-1
        start = 0
        end = n-1
        while start <= end:
            mid = (start + end) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                start = mid + 1
            else:
                end = mid - 1
        return start - 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3


import math


def main():
        T=int(input())
        while(T>0):
            
            NX=[int(x) for x in input().strip().split()]
            N=NX[0]
            X=NX[1]

            A=[int(x) for x in input().strip().split()]
            
            obj = Solution()
            print(obj.findFloor(A,N,X))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends