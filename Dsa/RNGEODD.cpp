#include <iostream>
using namespace std;

int main() {
    
	// your code goes here
	int a;
	int b;
	
	cin >> a;
	cin >> b;
	
	for(int i=a; i<=b; i++)
	{
	    if(i % 2 ==1)
	    {
	        cout << " " << i ;
	    }
	}
	return 0;
}
