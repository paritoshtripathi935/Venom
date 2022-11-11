"""
In the city, Kartik plans to launch a new fast-food chain. N days will see the center open. He is capable of preparing M various dishes. 
In order to make no more than K different sorts of foods over the course of the entire N days, he would like to cook.
how many ways is that possible for him?
nput pattern:

The first line contains the number of test cases. Then, each test case consists of a single line consisting of three space-separated integers N, M, K.

Output Pattern:

Integer - Number of way possible for

example:
input:
1
111
output:
1
"""
#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--)
	{
	    long long int n,m,k;
	    cin>>n>>m>>k;
	    if(n<k)
	    {
	        cout<<"0"<<endl;
	    }
	    else
	    {
	        long long int ans=1;
	        for(int i=0;i<k;i++)
	        {
	            ans=ans*(m-i);
	            ans=ans/(i+1);
	        }
	        cout<<ans<<endl;
	    }
	}
	return 0;
}

