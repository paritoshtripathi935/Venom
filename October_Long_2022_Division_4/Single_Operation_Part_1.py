"""
#include<bits/stdc++.h>
#define int long long
using namespace std;
void solve(){
   int n;string s;
   cin >> n >> s;
   for(int i=0;i<n;++i) 
      if(s[i]=='0') {
         cout << i << endl;
         return;
      }
   cout << n << endl;
}
signed main() {
   int T;cin >> T;
   while(T--) solve();
}

"""

# convert above cpp code into python

def SOP_ONE(n,s):
    for i in range(n):
        if s[i] == '0':
            return i
    return n

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = str(input())
        print(SOP_ONE(n,s))
    

if __name__ == "__main__":
    main()

