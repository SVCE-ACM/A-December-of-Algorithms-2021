#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main()
{
    cout<< "Enter the no of cars"<<endl;
    ll n; cin>>n;
    ll s1[n],i;
    ll var1;
    cout<< "Enter the speed of cars"<<endl;
    for(i=0;i<n;i++)
    {
         cin>>s1[i];
    }
    stack<ll> ans;
    ans.push(s1[0]);
    for(i=1;i<n;i++)
    {
        ll var1=s1[i];
        if((ans.top()>0 && var1>0) || (ans.top()<0 && var1<0))
        {
            ans.push(var1);
        }
        else
        {
            while(1)
            {
                ll curr=ans.top();
                if((abs(var1))>(abs(curr)))
                {
                    ans.pop();
                }
                else if((abs(var1))==(abs(curr)))
                {
                    ans.pop();
                    break;
                }
                else
                {
                    break;
                }
            }
        }
    }
    stack<ll> temp1;
    while(!ans.empty())
    {
        temp1.push(ans.top());
        ans.pop();
    }
    while(!temp1.empty())
    {
        cout<<temp1.top()<< " ";
        temp1.pop();
    }
    return 0;
}
