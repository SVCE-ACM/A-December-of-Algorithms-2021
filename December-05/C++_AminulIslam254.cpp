#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main()
{
    ll n1,n2,i;
    cout<< "Enter the no of customers"<<endl;
    cin>>n1;
    cout<< "Enter the no of biscuits"<<endl;
    cin>>n2;
    queue<ll> customers,biscuits;
    cout<< "Enter the customers preferances"<<endl;
    for(i=0;i<n1;i++)
    {
        ll var;cin>>var;
        customers.push(var);
    }
    cout<< "Enter the biscuits types"<<endl;
    for(i=0;i<n2;i++)
    {
        ll var;cin>>var;
        biscuits.push(var);
    }

    ll ans=0;
    while(!customers.empty())
    {
        if(customers.front()==biscuits.front())
        {
            customers.pop();
            biscuits.pop();
        }
        else
        {
            queue<ll> temp1=customers;
            bool flag=false;
            while(!temp1.empty())
            {
                if(temp1.front()==biscuits.front())
                {
                    flag=true;
                    break;
                }
                temp1.pop();
            }
            if(flag)
            {
                customers.push(customers.front());
                customers.pop();
            }
            else
            {
                break;
            }

        }
    }
    if(!customers.empty())
    {
        ans+=customers.size();
    }
    cout<<ans<<endl;

    return 0;
}
