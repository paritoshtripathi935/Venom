"""
#include<bits/stdc++.h>
using namespace std;
int SOP(int n,string s)
{
    int i,c=0;
    for(i=0;i<n;i++){ 
        c++;
        if(s[i+1]=='1')break;
    }
    return c;
}

int main() {
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        string s;
        cin>>s;
        cout<<SOP(n,s)<<endl;
        
    }
  return 0;
}
"""
# convert above cpp code to python3

"""
input
4
2
10
2
11
3
101
3
110
"""

def SOP(n,s):
    c = 0
    for i in range(n):
        c += 1
        if s[i+1] == '1':
            break
    return c

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        # take binary string as input and convert it to list
        s = str(input())
        print(SOP(n,s))
    

if __name__ == '__main__':
    main()
