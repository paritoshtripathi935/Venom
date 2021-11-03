#include <iostream>
using namespace std;

int main() {
	// your code goes here
	
	int N;
	std::cin >> N;
	int arr[N];
	
	for(int i=1; i<=N; i++)
	{
	    cin >> arr[i];
	}
	
	for(int k=N; k>0; k--)
	{
	    cout << " " << arr[k];
	}
	return 0;
}
