#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll fun1(vector<string> s)
{
    ll i,count1=0;
    char j;
    ll n=s.size();
    ll a[26]={0};
    for(i=0;i<n;i++)
    {
        string temp1=s[i];
        for(j='a';j<='z';j++)
        {
            if(temp1.find(j)!=string::npos)
            {
                a[j-'a']++;
            }
        }
    }
    for(i=0;i<26;i++)
    {
        if(a[i]==n)
        {
            count1++;
        }
    }
    return count1;
}

int main()
{
    vector<string> s;
    int i,n;
    cout<< "Enter the no of elements"<<endl;cin>>n;
    cout<< "Enter the elements"<<endl;
    for(i=0;i<n;i++)
    {
        string temp1;
        cin>>temp1;
        s.push_back(temp1);
    }
    cout<<fun1(s)<<endl;

    return 0;
}
