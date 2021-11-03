#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int n;
	
	std::cin >> n;
	
	if(n % 5 == 0 || n % 2 == 0 && n % 3 == 0)
	{
	    cout << "YES";
	}
	else
	{
	    cout << "NO";
	}
	
	return 0;
}
