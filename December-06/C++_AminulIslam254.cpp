#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main()
{
    string s; cin>>s;
    vector<ll> posu;
    vector<ll> post;
    ll i;
    for(i=0;i<s.length();i++)
    {
        if(s[i]=='U')
        {
            posu.push_back(i);
        }
        else
        {
            post.push_back(i);
        }
    }
    ll ans=0,j;
    if(post.size()<=posu.size())
    {
        ll ind=posu[0];
        bool flag=false;
        for(i=0;i<posu.size();i++)
        {
            if(ind!=posu[i])
            {
                ll back1=posu.back();
                swap(s[ind],s[back1]);
                post.push_back(back1);
                sort(post.begin(),post.end());
                for(j=post[0];j<post.size()-1;j++)
                {
                    if((post[j]+1)!=post[j+1])
                    {
                        flag=true;
                        break;
                    }
                }
                ans++;
                if(!flag)
                {
                    break;
                }
                flag=false;
            }
            ind++;
        }
    }
    else
    {
        ll ind=post[0];
        bool flag=false;
        for(i=0;i<post.size();i++)
        {
            if(ind!=post[i])
            {
                ll back1=post.back();
                swap(s[ind],s[back1]);
                posu.push_back(back1);
                sort(posu.begin(),posu.end());
                for(j=posu[0];j<posu.size()-1;j++)
                {
                    if((posu[j]+1)!=posu[j+1])
                    {
                        flag=true;
                        break;
                    }
                }
                ans++;
                if(!flag)
                {
                    break;
                }
                flag=false;
            }
            ind++;
        }
    }
    cout<<ans<<endl;
    return 0;
}
