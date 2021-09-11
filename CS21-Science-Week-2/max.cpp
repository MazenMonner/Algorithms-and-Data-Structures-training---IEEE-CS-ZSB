#include <bits/stdc++.h>
typedef long long int ll;
const unsigned int MOD = 1000000007;
 
using namespace std;
 
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int t;
    cin>>t;
    while(t--)
    {
        ll n,a,b;
        cin>>n>>a>>b;
 
        string s;
        cin>>s;
 
        ll c=1;
 
        for (int i = 1; i < n; i++)
        {
            if (s[i] != s[i - 1])
                c++;
        }
 
        if(b>=0)
        {
            cout<<n*(a+b)<<"\n";
            continue;
        }
        else
        {
            cout << (c / 2 + 1) * b + a * n << "\n";
        }
 
 
    }
#ifndef ONLINE_JUDGE
    cerr << "Time : " << 1000 * ((double)clock()) / (double)CLOCKS_PER_SEC << "ms\n";
#endif
    return 0;
}