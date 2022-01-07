#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main()
{
    cout<< "Enter the no of test cases"<<endl;
    ll t; cin>>t;
    while(t--)
    {
        ll x;
        cout<< "Enter the no of rangers"<<endl;

        cin>>x;
        ll a[x],i;
        cout<< "Enter the position of the rangers"<<endl;
        ll odd1=0,even1=0;
        for(i=0;i<x;i++)
        {
            cin>>a[i];
            if(a[i]%2==0)
            {
                even1++;
            }
            else
            {
                odd1++;
            }
        }
        cout<< "Enter the position of leo"<<endl;
        ll pos; cin>>pos;
        if(odd1==0 || even1==0)
        {
            cout<<x<< " "<<1<<endl;
        }
        else
        {
            if(odd1>even1)
            {
                cout<<odd1<< " "<<-1<<endl;
            }
            else
            {
                cout<<even1<< " "<<-1<<endl;
            }
        }

    }

    return 0;
}
