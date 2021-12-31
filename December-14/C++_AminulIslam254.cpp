#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main()
{
    cout<< "Enter the no chapters"<<endl;
    ll n; cin>>n;
    ll a[n],i,sum1=0,j;
    cout<< "Enter the no of concepts for each chapter"<<endl;
    for(i=0;i<n;i++)
    {
        cin>>a[i];
    }
    cout<< "Enter the value of x"<<endl;
    ll x; cin>>x;
    sort(a,a+n);
    if(n==x)
    {
        cout<<a[n-1]<<endl;
    }
    else
    {
        for(i=n-2;i>=0;i--)
        {
            ll time1=i+1;
            sum1+=a[i+1];
            ll rem=sum1%a[i];
            if(rem==0)
            {
                time1+=(sum1/a[i]);
            }
            else
            {
                 time1+=(sum1/a[i])+1;
            }
            bool flag=false;
            if(time1>=x)
            {
                time1=i+1;
                for(j=a[i]+1;j<=a[i+1];j++)
                {
                    rem=sum1%j;
                    if(rem==0)
                    {
                        time1+=(sum1/j);
                    }
                    else
                    {
                         time1+=(sum1/j)+1;
                    }
                    if(time1<x)
                    {
                        cout<<j<<endl;
                        flag=true;
                        break;
                    }
                }
            }
            if(flag)
            {
                break;
            }
        }
    }
    return 0;
}
