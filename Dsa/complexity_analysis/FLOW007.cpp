#include <iostream>

using namespace std;

int main()
{
    int n,m;
    
    cin>>n;
    for(int i=0;i<n;i++)
    {
        bool zero=true;
        cin>>m;
        while(m>0)
        {
            if (m%10==0 and zero==true)
            {
                m=m/10;
                continue;
            }
            else
            {
                zero=false;
                cout<<m%10;
                m=m/10;
            }
        }
        cout<<"\n";
    }
    return 0;
}
