#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main()
{
    cout<< "Enter the size for each task"<<endl;
    ll n; cin>>n;
    ll task_size[n],process_time[n],noof_task[n],i;
    cout<< "Enter the elements for task size"<<endl;
    for(i=0;i<n;i++)
    {
        cin>>task_size[i];
    }
    cout<< "Enter the elements for processing time"<<endl;
    for(i=0;i<n;i++)
    {
        cin>>process_time[i];
    }
    cout<< "Enter the elements for no of tasks"<<endl;
    for(i=0;i<n;i++)
    {
        cin>>noof_task[i];
    }
    ll ans=0,time1=0;
    for(i=0;i<n;i++)
    {
        time1=noof_task[i]/task_size[i];
        if(noof_task[i]%task_size[i]!=0)
        {
            time1++;
        }
        ans=max(ans,(time1*process_time[i]));
    }
    cout<<ans<<endl;
    return 0;
}
