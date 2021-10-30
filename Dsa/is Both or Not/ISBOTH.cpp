#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int N;
	cin >> N;
	
	if((N % 5 == 0 && N % 11 != 0) || (N % 5 != 0 && N % 11 == 0))
	{
	    std::cout << "ONE" << std::endl;
	}
	else if((N % 5 == 0) && (N % 11 == 0))
	{
	    cout << "BOTH" << endl;
	}
	else
	{
	    cout << "NONE" << endl;
	}
	return 0;
}
