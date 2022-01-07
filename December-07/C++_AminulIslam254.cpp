#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main()
{
    ll n;
    cout<< "Enter the no of buildings"<<endl;
    cin>>n;
    ll a[n][6],i,j;
    cout<< "Enter coordinates"<<endl;
    for(i=0;i<n;i++)
    {
        for(j=0;j<6;j++)
        {
            cin>>a[i][j];
        }
    }
    ll num,k;
    cout<< "Enter the no of jet planes"<<endl;
    cin>>num;
    ll store1=0;
    for(k=0;k<num;k++)
    {
        cout<< "Enter axis either x or y"<<endl;
        char c; cin>>c;
        cout<< "Enter axis number for x or y"<<endl;
        ll axisnum;cin>>axisnum;
        for(i=0;i<n;i++)
        {
            bool issmall=false;
            bool isbig=false;
            if(c=='x') j=0;
            if(c=='y') j=1;
            for(;j<6;j+=2)
            {
                if(a[i][j]<axisnum)
                {
                    issmall=true;
                }
                else if(a[i][j]>axisnum)
                {
                    isbig=true;
                }
            }
            if(issmall && isbig)
            {
                store1++;
            }
        }
        cout<<store1<<endl;
        store1=0;
    }

    return 0;
}
