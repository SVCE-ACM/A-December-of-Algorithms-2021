#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main()
{
    cout<< "Enter the no of diamonds"<<endl;
    ll x; cin>>x;
    vector<ll> mp,np;
    ll i,var1;
    cout<< "Enter the purity levels of all diamonds"<<endl;
    for(i=0;i<x;i++)
    {
        cin>>var1;
        mp.push_back(var1);
    }
    cout<< "Enter the minimum prices of all diamonds"<<endl;
    for(i=0;i<x;i++)
    {
        cin>>var1;
        np.push_back(var1);
    }
    cout<< "Enter the no of clients"<<endl;
    ll z; cin>>z;
    ll k[z],r[z],j;
    cout<< "Enter the values of k"<<endl;
    for(i=0;i<z;i++)
    {
        cin>>k[i];
    }
    cout<< "Enter the values of r"<<endl;
    for(i=0;i<z;i++)
    {
        cin>>r[i];
    }
    ll ans=0;
    for(i=0;i<z;i++)
    {
        for(j=0;j<mp.size();j++)
        {
            if(mp[j]>k[i] && np[j]<=r[i])
            {
                ans++;
                mp.erase(mp.begin()+j);
                np.erase(np.begin()+j);
                break;
            }
        }
    }
    cout<<ans<<endl;
    return 0;
}
