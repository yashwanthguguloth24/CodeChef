//https://www.codechef.com/APRIL21C/problems/BOLT

#include <iostream>
using namespace std;

float round(float var)
{
    // 37.66666 * 100 =3766.66
    // 3766.66 + .5 =3767.16    for rounding off value
    // then type cast to int so value is 3767
    // then divided by 100 so the value converted into 37.67
    float value = (int)(var * 100 + .5);
    return (float)value / 100;
}



int main() {
	int t;
	cin >> t;
	while(t--)
	{
	    float k1,k2,k3,v;
	    float v1,chef_time;
	    cin >> k1 >> k2 >> k3 >> v;
	    v1 = k1*k2*k3*v;
	    float bolt = 9.58;
	    chef_time = 100/v1;
	    if (round(chef_time) >= bolt)
	    {
	        //cout << round(chef_time) << endl;
	        cout <<  "NO" << endl;
	    }
	    else
	    {
	        //cout << round(chef_time) << endl;
	        cout << "YES" << endl;
	    }

	}
	return 0;
}
