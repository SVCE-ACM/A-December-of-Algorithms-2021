#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void makegraph(vector<set<ll>> &v1,ll a,ll b)
{
    v1[a].insert(b);
    v1[b].insert(a);
}

void fun1(vector<set<ll>>& v1,ll head,ll &count1)
{
    for(auto x:v1[head])
    {
        if(x==1)
        {
            count1++;
            v1[head].erase(v1[head].begin());
            return;
        }
        else
        {
            fun1(v1,x,count1);
        }
    }
    return;
}

int main()
{

    cout<< "Enter the value of x and y"<<endl;
    ll x,y,i; cin>>x>>y;
    vector<set<ll>> v1(y+1);
     cout<< "Enter the values of a and b"<<endl;
    for(i=0;i<y;i++)
    {
        ll a,b; cin>>a>>b;
        makegraph(v1,a,b);
    }
    ll count1=0;
    fun1(v1,1,count1);
    cout<<count1<<endl;
    return 0;
}
