# Yashwanth
# 28/3/2021


for _ in range(int(input())):
    N,M = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    flag_arr = [0]*M
    for i in range(N):
        flag_arr[arr[i]-1] = 1
    flag = False
    for j in range(M):
        if flag_arr[j] == 0:
            flag = True
    if flag == True:
        print('Yes')
    else:
        print('No')
