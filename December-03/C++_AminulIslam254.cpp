#include <bits/stdc++.h>

using namespace std;

typedef long long ll;


int fun1(vector<vector<char>> a,string s,string name,ll i,ll j,ll r,ll c)
{
    if(s.length()>name.length())
    {
        return 0;
    }
    if(i>=r)
    {
        return 0;
    }
    if(j>=c)
    {
        return 0;
    }
    if(s==name)
    {
        return 1;
    }
    int m1=(fun1(a,s+a[i][j],name,i,j+1,r,c));
    int m2=(fun1(a,s,name,i+1,j,r,c));
    int m3=(fun1(a,s,name,i,j+1,r,c));
    int m4=(fun1(a,s+a[i][j],name,i+1,j,r,c));
    return m1+m2+m3+m4;
}

int main()
{
    ll r,c;
    cout<< "Enter the no of rows"<<endl;
    cin>>r;
    cout<< "Enter the no of coloumns"<<endl;
    cin>>c;
    vector<vector<char>>a;
    ll i,j;
    cout<< "Enter elements"<<endl;
    for(i=0;i<r;i++)
    {
        vector<char>temp1;
        for(j=0;j<c;j++)
        {
            char c; cin>>c;
            temp1.push_back(c);
        }
        a.push_back(temp1);
    }
    string s="";
    string name;
    cout<< "Enter name"<<endl;
    cin>>name;
    if(fun1(a,s,name,0,0,r,c))
    {
        cout<< "YES"<<endl;
    }
    else
    {
        cout<< "NO" <<endl;
    }
    return 0;
}
