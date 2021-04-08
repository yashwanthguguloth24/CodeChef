// https://www.codechef.com/APRIL21C/problems/MEXSTR
// Partially correct solution



#include <iostream>
#include <cmath>
#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;

string toBinary(ll n) 
{
    if (n==0) return "0";
    else if (n==1) return "1";
    else if (n%2 == 0) return toBinary(n/2) + "0";
    else if (n%2 != 0) return toBinary(n/2) + "1";
}



bool isSubSequence(string str1,string str2)
{
    ll m = str1.length();
    ll n = str2.length();
    ll j = 0;
    ll i = 0;
    while(j < m && i < n)
    {
        if (str1.at(j) == str2.at(i))
        {
            j++;
        }
        i++;
    }
    return j==m;
}

int main() {
	int t;
	cin >> t;
	while(t--)
	{
	    string b_str;
	    cin >> b_str;
	    ll L = b_str.length();
	    bool cFlag = false;
	    ll buffer = 0;
	    for(ll i=0;i<pow(2,L);i++)
	    {
	        string bin_val = toBinary(i);
	        if (isSubSequence(bin_val,b_str))
	        {
	            cFlag = true;
	        }
	        else
	        {
	            buffer = i;
	            break;
	        }
	    }
	    string val = toBinary(buffer);
	    cout << val << endl;
	}
	return 0;
}
