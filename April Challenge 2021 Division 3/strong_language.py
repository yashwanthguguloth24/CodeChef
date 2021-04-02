# https://www.codechef.com/APRIL21C/problems/SSCRIPT

for _ in range(int(input())):
    N,K = list(map(int,input().split()))
    s_list = list(input())
    s = "".join(s_list)
    targ_list = ['*']*K 
    targ = "".join(targ_list)
    flag = False
    i = 0
    while i < N-K+1:
        if s[i] == "*":
            if s[i:i+K] == targ:
                flag = True
                i = i+K
        i = i+1
    if flag:
        print("YES")
    else:
        print("NO")
