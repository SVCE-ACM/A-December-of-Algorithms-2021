#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main()
{
    ll n,p,i;
    cout<< "Enter the value of n and p"<<endl;
    cin>>n>>p;
    vector<ll> a;
    cout<< "Enter array elements"<<endl;
    for(i=0;i<n;i++)
    {
        ll var1; cin>>var1;
        a.push_back(var1);
    }
    sort(a.begin(),a.end());
    vector<ll> temp1;
    for(i=0;i<n-1;i++)
    {
        temp1.push_back(a[i+1]-a[i]);
    }
    ll min1=INT_MAX,index=-1;
    for(i=0;i<temp1.size();i++)
    {
        if(temp1[i]<min1)
        {
            min1=temp1[i];
            index=i;
        }
    }
    vector<ll> v1;
    if(index==0)
    {
        for(i=0;i<p;i++)
        {
            v1.push_back(a[i]);
        }
    }
    else if(index==n-1)
    {
        for(i=n-1;i>=p;i--)
        {
            v1.push_back(a[i]);
        }
    }
    else
    {
        v1.push_back(a[index+1]);
        ll left=index-1,right=index+1;
        p=p-1;
        while(p)
        {
            if(left==-1)
            {
                v1.push_back(a[right]);
                right++;
            }
            else if(right==n)
            {
                v1.push_back(a[left]);
                left--;
            }
            else
            {
                if((a[index]-a[left])<(a[right]-a[index]))
                {
                    v1.push_back(a[left]);
                    left--;
                }
                else
                {
                    v1.push_back(a[right]);
                    right++;
                }
            }
            p--;
        }
    }
    sort(v1.begin(),v1.end());
    ll num1=v1[v1.size()-1],ans=0;
    for(i=v1.size()-2;i>=0;i--)
    {
        ans+=(num1-v1[i]);
    }
    cout<<ans<<endl;
    return 0;
}
