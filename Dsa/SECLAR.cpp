#include <iostream>
using namespace std;

int main() {
	// your code goes here
	// intialize the array a
	int A[3];
	
	for(int i = 0;i<=3;i++)
	{
	    cin >> A[i];
	}
	
	// find the length of array 
	
	int n = sizeof(A) / sizeof(A[0]) ;
	
	for (int i = 0; i < n; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            if (A[i] < A[j])
            {
                int x = A[i];
                A[i] = A[j];
                A[j] = x;
            }
        }
    }
    
    cout << A[1];
    
	return 0;
}

