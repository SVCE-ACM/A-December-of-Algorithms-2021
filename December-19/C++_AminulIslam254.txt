#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main()
{
    cout<< "Enter the size of matrix"<<endl;
    ll n,i,j; cin>>n;
    cout<< "Enter the courses"<<endl;
    vector<set<ll>> v1(n);
    for(i=0;i<n;i++)
    {
        ll a1,a2;
        cin>>a1>>a2;
        for(auto x:v1[a1])
        {
            v1[i].insert(a2);
        }
        v1[a1].insert(a2);

    }
    cout<< "Enter the size for the answer matrix"<<endl;
    ll size1; cin>>size1;
    vector<bool> ans;
    cout<< "Enter the elements for the answer matrix"<<endl;
    for(i=0;i<size1;i++)
    {
        ll a1,a2;
        cin>>a1>>a2;
        if(v1[a1].count(a2))
        {
            ans.push_back(true);
        }
        else
        {
            ans.push_back(false);
        }
    }
    for(i=0;i<ans.size();i++)
    {
        cout<<ans[i]<< " ";
    }
    return 0;
}
