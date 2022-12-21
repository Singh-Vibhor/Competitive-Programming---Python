#include <bits/stdc++.h>
using namespace std;
#define ll long long int

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        map<int,int> m;
        ll n;
        cin>>n;
        string s;
        cin>>s;
        int prv=0;
        ll ans=0;
        for (ll i=0; i<n; i++){
            if (s[i]=='0')
            {
                if (prv==0)
                {
                    ans+=i+1;
                    m[i+1]+=1;
                    prv=i+1;
                }
                else
                {
                    int f=0;
                    for(auto it: m){
                        if ((i+1)%it.first==0){
                            if ((i+1)/it.first==(it.second+1) && f==0){
                            ans+=it.first;
                            m[it.first]+=1;
                            m[i+1]+=1;
                            f=1;}

                            else if((i+1)/it.first==(it.second+1)){
                                m[it.first]+=1;
                            }

                        }
                        
                    }
                    if (f==0){
                        ans+=i+1;
                        m[i+1]+=1;
                    }
                }
            }
        }
        cout<<ans<<endl;
    }
    
}