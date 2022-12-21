#include<bits/stdc++.h>
using  namespace  std;

#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;

#define ordered_set tree<int, null_type,less<int>, rb_tree_tag,tree_order_statistics_node_update>

#define faster  ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

#define sq(x)   (x)*(x)
#define PI      acos(-1.0)
#define all(x) x.begin(),x.end()
#define nl      '\n'
#define mod 1000000007
typedef long long int ll;
typedef unsigned long long int  llu;


int dy[]={0,1,0,-1};

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        int ar[n+3];
        ll sum=0;
        vector<ll>v1,v2;
        for(int i=0;i<n;i++)
        {
            cin>>ar[i];
        }
        v1.push_back(ar[0]);
        v2.push_back(ar[0]);
        for(int i=1;i<n;i++)
        {
            int x=v1.size()-1;
            v1.push_back(v1[x]+ar[i]);
            if(v2[x]>=ar[i])v2.push_back(v2[x]-ar[i]);
            else v2.push_back(v2[x]+ar[i]);
        }
        if(v1!=v2)cout<<-1<<endl;
        else
        {
            for(int i=0;i<n;i++)
            {
                cout<<v1[i]<<" ";
            }
            cout<<endl;
        }
    }
}

