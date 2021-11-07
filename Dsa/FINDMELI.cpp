#include<bits/stdc++.h>
using namespace std;
bool present(int arr[],int n,int k)
{
    for(int i=0;i<n;i++)
    {
        if(arr[i]==k)
            return true;
    }
    return false;
}
int main()
{
    int n,k;
    cin>>n>>k;
    int arr[n];
    for(int i=0;i<n;i++)
        cin>>arr[i];
    if(present(arr,n,k))
        cout<<"1"<<endl;
    else
        cout<<"-1"<<endl;
}