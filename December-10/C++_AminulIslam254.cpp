#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void fun1(vector<vector<ll>> a,ll n,ll& count1,bool& isend,ll i,ll j,vector<vector<bool>>& maze1)
{
    if(i==n)
    {
        return;
    }
    if(j==n)
    {
        return;
    }
    if(i==n-1 && j==n-1)
    {
        isend=true;
    }
    if(a[i][j]==1 && (!maze1[i][j]))
    {
        count1++;

    }
    maze1[i][j]=true;
    if(a[i][j]==-1)
    {
        return;
    }
    fun1(a,n,count1,isend,i+1,j,maze1);
    fun1(a,n,count1,isend,i,j+1,maze1);
}

int main()
{
    cout<< "Enter the no of rows and coloumns"<<endl;
    ll n; cin>>n;
    vector<vector<ll>> a;
    ll i,j;
    cout<< "Enter the elements"<<endl;
    for(i=0;i<n;i++)
    {
        vector<ll> temp1;
        for(j=0;j<n;j++)
        {
            ll var1; cin>>var1;
            temp1.push_back(var1);
        }
        a.push_back(temp1);
    }
    ll count1=0;
    bool isend=false;
    vector<vector<bool>> maze1;
    for(i=0;i<n;i++)
    {
        vector<bool>temp2;
        for(j=0;j<n;j++)
        {
            temp2.push_back(false);
        }
        maze1.push_back(temp2);
    }
    fun1(a,n,count1,isend,0,0,maze1);
    if(isend)
    {
        cout<<count1<<endl;
    }
    else
    {
        cout<<0<<endl;
    }
    return 0;
}
