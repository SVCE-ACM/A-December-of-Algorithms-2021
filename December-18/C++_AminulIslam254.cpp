#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main()
{
    cout<< "Enter the size of matrix"<<endl;
    ll n; cin>>n;
    ll a[n][n],i,j;
    ll pos[2][2],k=0;
    cout<< "Enter the no of elements"<<endl;
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            cin>>a[i][j];
            if(a[i][j]==1)
            {
                pos[k][0]=i;
                pos[k][1]=j;
                k++;
            }
        }
    }
    cout<<abs(pos[1][0]-pos[0][0])+abs(pos[1][1]-pos[0][1])-1<<endl;
    return 0;
}
