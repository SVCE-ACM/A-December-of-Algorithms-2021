#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main()
{
    ll n;
    cout<< "Enter the time"<<endl;
    cin>>n;
    ll a[n+1]={0},i,current1=3;
    a[1]=3;
    for(i=2;i<=n;i++)
    {
        if(a[i-1]==1)
        {
            current1*=2;
            a[i]=current1;
        }
        else
        {
            a[i]=a[i-1]-1;
        }
    }
    cout<<a[n]<<endl;


    return 0;
}
