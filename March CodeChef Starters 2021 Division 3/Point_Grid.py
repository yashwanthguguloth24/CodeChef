# Yashwanth 
# 28/2/2021
# Point Grid code


for _ in range(int(input())):
    N = int(input())
    cols = [int(x) for x in input().split()]
    ans = cols[-1]
    for i in reversed(range(0,N-1)):
        maxi = cols[i+1]-1
        if cols[i] <= maxi:
            continue
        ans += cols[i]-maxi
    print(ans)


