#include<bits/stdc++.h>
using namespace std;


int main(){
    long long int t;
    cin>>t;
    while(t--){
        long long int n,x;
        cin>>n>>x;
        if (n%x!=0){
            cout<<-1<<endl;
        }
        else{
            cout<<x<<" ";
            for (int i=2;i<n;i++){
                if (i==x){
                    int f=1,a=2;
                    while(a*x<=n){
                        cout<<x*a<<" ";
                        x*=a;
                        f=0;break;
                    }
                    if (f) cout<<n<<" ";
                }
                else{
                    cout<<i<<" ";
                }
            }
            cout<<1<<endl;
        }
    }    
}