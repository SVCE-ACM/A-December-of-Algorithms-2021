#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main()
{
    cout<< "Enter the value of n"<<endl;
    ll n,i; cin>>n;
    cout<< "Enter the size of the load"<<endl;
    ll size1;cin>>size1;
    ll load[size1];
    cout<< "Enter the load of all the processes"<<endl;
    for(i=0;i<size1;i++)
    {
        cin>>load[i];
    }
    int server[n]={0},j,count1[n]={0};
    for(i=0;i<size1;i++)
    {
        for(j=0;j<n;j++)
        {
            server[j]-=1;
        }
        ll temp1=load[i]%n;
        if(server[temp1]!=0)
        {
            bool flag=false;
            for(j=(temp1+1)%n;j<n;j++)
            {
                j=j%n;
                if(server[j]==0)
                {
                    flag=true;
                    server[j]=load[i];
                    count1[j]++;
                    break;
                }
            }
            if(!flag)
            {
                int min1=INT_MAX,index1=0;
                for(j=0;j<n;j++)
                {
                    if(server[j]<min1)
                    {
                        min1=server[j];
                        index1=j;
                    }
                }
                for(j=0;j<n;j++)
                {
                    server[j]-=min1;
                }
                server[index1]=load[i];
                count1[index1]++;
            }

        }
        else
        {
            server[temp1]=load[i];
            count1[temp1]++;
        }
    }
    int ans=-1,index1=-1;
    for(i=0;i<n;i++)
    {
        if(count1[i]>ans)
        {
            ans=count1[i];
            index1=i;
        }
    }
    cout<<index1<<endl;
    return 0;
}
