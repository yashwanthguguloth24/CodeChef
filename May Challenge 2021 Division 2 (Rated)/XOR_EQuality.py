#https://www.codechef.com/MAY21B/problems/XOREQUAL


# GFG Reference for Modular Exponentiation
# https://www.geeksforgeeks.org/modular-exponentiation-power-in-modular-arithmetic/


def power(x, y, p) :
    res = 1     # Initialize result
 
    # Update x if it is more
    # than or equal to p
    x = x % p
     
    if (x == 0) :
        return 0
 
    while (y > 0) :
         
        # If y is odd, multiply
        # x with result
        if ((y & 1) == 1) :
            res = (res * x) % p
 
        # y must be even now
        y = y >> 1      # y = y/2
        x = (x * x) % p
         
    return res
     
for _ in range(int(input())):
    N = int(input())
    # answer is 2^(N-1) because x is an even number and 2^(N-1) even numbers in 2^N window
    fans = power(2,N-1,10**9+7)
    print(fans)
