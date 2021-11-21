#include <iostream>
#include <cmath>
using namespace std;

int main() {
	// your code goes here
	int a;
	int b;
	int c;
	std::cin >> a >> b >> c;


	if(a + b <= c || a + c <= b || b + c <= a)
	{
	    std::cout << "NO" << std::endl;
	}
	else
	{
	    cout << "YES" ;
	}
	return 0;
}
