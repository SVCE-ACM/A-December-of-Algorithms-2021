#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

bool fun1(ll n)
{
    unordered_set<ll> s1;
    while(1)
    {
        ll temp1=0;
        while(n)
        {
            temp1+=((n%10)*(n%10));
            n/=10;
        }
        if(temp1==1)
        {
            return true;
        }
        if(s1.count(temp1))
        {
            return false;
        }
        s1.insert(temp1);
        n=temp1;
    }
}

int main()
{
    ll n;
    cout<< "Enter the element"<<endl;
    cin>>n;
    if(fun1(n))
    {
        cout<< "YES"<<endl;
    }
    else
    {
        cout<< "NO" <<endl;
    }

    return 0;
}
