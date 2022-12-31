#Implement pow(x, n) % M.
#In other words, given x, n and M, find (xn) % M.

class Solution:
	def PowMod(self, x, n, m):
        		# code here
		if n==0:
		    return 1
		elif n%2==0:
		    y=self.PowMod(x,n//2,m)
		    return (y*y)%m
		else:
		    return (x*self.PowMod(x,n-1,m))%m


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		x, n , m = input().split()
		x = int(x)
		n = int(n) 
		m = int(m)
		ob = Solution();
		ans = ob.PowMod(x, n, m)
		print(ans)
# } Driver Code Ends