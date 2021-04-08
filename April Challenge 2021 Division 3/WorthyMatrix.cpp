// https://www.codechef.com/APRIL21C/problems/KAVGMAT


#include <bits/stdc++.h>
#include <iostream>
using namespace std;
typedef long long int ll;

ll min(ll a, ll b)
{
    if(a<b)
    {
        return a;
    }
    else
    {
        return b;
    }
}

int main() {
	ll t;
	cin >> t;
	while(t--)
	{
	    ll N,M,K;
	    cin >> N >> M >> K;
	    double mat[N+1][M+1];
	    for(ll i=0;i<=N;i++)
	    {
	        for(ll j = 0;j<=M;j++)
	        {
	            if(i == 0 || j == 0)
	            {
	                mat[i][j] = 0;
	            }
	            else
	            {
	                cin >> mat[i][j]; 
	            }
	        }
	    }
	    
	    for(ll i=0;i<=N;i++)
	    {
	        ll cumSum = 0;
	        for(ll j = 0;j<=M;j++)
	        {
	            cumSum += mat[i][j];
	            mat[i][j] = cumSum;
	        }
	    }	    

	    for(ll j=0;j<=M;j++)
	    {
	        ll cumSum = 0;
	        for(ll i = 0;i<=N;i++)
	        {
	            cumSum += mat[i][j];
	            mat[i][j] = cumSum;
	            //cout << mat[i][j] ;
	        }
	        //cout << endl;
	    }
	    
	    ll result = 0;
	    ll Z = min(N,M);
	    for(ll l=1;l<=Z;l++)
	    {
	        for(ll i=l;i<=N;i++)
	        {
	            for(ll j=l;j<=M;j++)
	            {
	                if(((mat[i][j]+mat[i-l][j-l]-mat[i-l][j]-mat[i][j-l])/(l*l)) >= K)
	                {
	                    result++;
	                }
	            }
	        }
	    }
	    cout << result << endl;
	    
	    
	}
	return 0;
}
