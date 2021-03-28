# Yashwanth
# 28/3/2021

for _ in range(int(input())):
    NFoot,MCric = [int(x) for x in input().split()]
    F = [int(x) for x in input().split()]
    C = [int(x) for x in input().split()]
    iFoot = 0
    jCric = 0
    flag = 0 # 0-foot 1-Cric
    num_switch = 0
    while iFoot < NFoot and jCric < MCric:
        if F[iFoot] < C[jCric]:
            if flag == 1:
                num_switch += 1
            flag = 0
            iFoot += 1
        else:
            if flag == 0:
                num_switch += 1
            flag = 1
            jCric += 1
            
    while iFoot < NFoot:
        if flag == 0:
            break
        else:
            num_switch += 1
            flag = 0
            iFoot += 1
            
    while jCric < MCric:
        if flag == 1:
            break
        else:
            num_switch += 1
            flag = 1
            jCric += 1  
            
    print(num_switch)
