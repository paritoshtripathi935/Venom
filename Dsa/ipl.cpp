///
//Indian Premier League tickets are limited so, the Indian Government gives two random numbers a and b to the Dubai Government. 
//Dubai Government wants to give the ticket to all candidates with IDs between a and b ( both inclusive ), 
// However, due to coronavirus pandemic time Government can't give tickets to every candidate, Dubai Government decides to give the ticket to candidates having special ID,


// A special ID is not divisible by any number of the form p*p where (p>1).
// So your task is to find the number of candidates getting the tickets.


//1
//1 10

// Output

//7

// start code here

#include <iostream>
using namespace std;
int main() {
    int t;
    cin>>t;
    while(t--)
    {
        int a,b;
        cin>>a>>b;
        int count=0;
        for(int i=a;i<=b;i++)
        {
            int flag=0;
            for(int j=2;j*j<=i;j++)
            {
                if(i%(j*j)==0)
                {
                    flag=1;
                    break;
                }
            }
            if(flag==0)
            {
                count++;
            }
        }
        cout<<count<<endl;
    }
    return 0;
}

// end code here

If you get any error in the above code then please comment down below.

Please enter your name here

You have entered an incorrect email address
//end code here

// Sample input
// 1
// 1 10

// Sample Output
// 7

// Time Complexity: O(n)
// Space Complexity: O(1)

// Explanation
// There are 7 prime numbers between 1 and 10.

// Test Cases
// 1
// 1 10
// 2
// 1 100
// 3
// 1 1000
// 4
// 1 10000
// 5
// 1 100000
// 6
// 1 1000000
// 7
// 1 10000000
// 8
// 1 100000000
// 9
// 1 1000000000
// 10
// 1 10000000000
// 11
// 1 100000000000
// 12
// 1 1000000000000
// 13
// 1 10000000000000
// 14
// 1 100000000000000
// 15
// 1 1000000000000000
// 16
// 1 10000000000000000
// 17
// 1 100000000000000000
// 18
// 1 1000000000000000000

// Author
// Name: Prateek Bajpai
// Profile: https