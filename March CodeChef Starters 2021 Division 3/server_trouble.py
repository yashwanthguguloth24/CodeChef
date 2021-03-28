# Yashwanth
# 28/3/2021


import math
for _ in range(int(input())):
    N,K = [int(x) for x in input().split()]
    mpms = math.ceil(N/K)
    if N%K == 0:
        num_rep = K
    else:
        num_rep = N%K
    print(mpms,num_rep)
