//https://www.codechef.com/APRIL21C/problems/SSCRIPT


#include <iostream>
#include <string>
using namespace std;

int main() {
	int t;
	cin >> t;
	while(t--)
	{
	    int N,K;
	    cin >> N >> K;
	    string s;
	    cin >> s;
	    int ans = 0;
	    char targ = '*';
	    for(int i = 0;i<N;i++)
	    {
	        if(s.at(i) == targ)
	        {
	            int j = i+1;
	            int cntr = 1;
	            while((j<N) && (s.at(j) == targ))
	            {
	                cntr++;
	                j++;
	            }
	            i = j;
	            ans = max(cntr,ans);
	        }
	    }
	    if(ans >= K)
	    {
	        cout << "YES" <<  endl;
	    }
	    else
	    {
	        cout << "NO" << endl;
	    }
	}
	return 0;
}
