#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main()
{
    cout<< "Enter the no bracelts"<<endl;
    ll x; cin>>x;
    ll a[x],i,sum1=0,time1=0,max1=-1;
    cout<< "Enter the array"<<endl;
    for(i=0;i<x;i++)
    {
        cin>>a[i];
        sum1+=a[i];
        max1=max(max1,a[i]);
    }
    cout<< "Enter the value of n"<<endl;
    ll n; cin>>n;
    for(i=max1;;i++)
    {
        time1=sum1/i;
        if(sum1%i!=0)
        {
            time1++;
        }
        if(time1<=n)
        {
            cout<<i<<endl;
            break;
        }

    }

    return 0;
}
