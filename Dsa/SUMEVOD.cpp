#include <bits/stdc++.h>
using namespace std;
 
// function to find sum of
// first n even numbers
int evenSum(long long n)
{
    // required sum
    return (n * (n + 1));
}

int oddsum(long long n)
{
    return (n*n);
} 
 
// Driver program to test above
int main()
{
    long long n;
    std::cin >> n;
    
    cout << oddsum(n) << " " << evenSum(n);
    return 0;
}
