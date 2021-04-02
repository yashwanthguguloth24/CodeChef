# https://www.codechef.com/APRIL21C/problems/SOCKS1

socks = list(map(int,input().split()))
socks_set = set(socks)
if len(socks_set) == 3:
    print("NO")
else:
    print("YES")

