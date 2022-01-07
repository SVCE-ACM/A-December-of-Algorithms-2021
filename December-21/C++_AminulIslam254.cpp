#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main()
{

    cout<< "Enter the value of x"<<endl;
    ll x; cin>>x;
    ll a[x][x],i,j,noof1s=0,noof0s=0;
    cout<< "Enter the elements of array"<<endl;
    for(i=0;i<x;i++)
    {
        for(j=0;j<x;j++)
        {
            cin>>a[i][j];
            if(a[i][j])
            {
                noof1s++;
            }
            else
            {
                noof0s++;
            }
        }
    }
    ll var1=(x*x)/2;
    ll var2=(x*x)-var1;
    if(var1==noof0s && var2==noof1s)
    {
        ll col0=0,flag=0;
        for(i=0;i<x;i++)
        {
            for(j=0;j<x;j++)
            {
               if(!a[j][i])
               {
                   col0++;
               }
            }
            if(col0!=(x/2))
            {
                flag=1;
                break;
            }
            col0=0;
        }
        if(flag)
        {
            cout<<-1<<endl;
        }
        else
        {
            ll anomaly=0,count1=1;
            j=1;
            for(i=0;i<x;i++)
            {
                for(;j<x;j+=2)
                {
                   if(!a[j][i])
                   {
                       anomaly++;
                   }
                }
                if(count1)
                {
                    count1=0;
                    j=0;
                }
                else
                {
                    count1=1;
                    j=1;
                }
            }
            if(anomaly==0)
            {
                cout<<0<<endl;
            }
            else
            {
                cout<<anomaly/2<<endl;
            }
        }
    }
    else
    {
        cout<<-1<<endl;
    }

    return 0;
}
