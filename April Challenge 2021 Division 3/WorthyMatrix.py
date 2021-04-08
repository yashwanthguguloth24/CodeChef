# My solution for worthy matrix problem


import numpy as np
for _ in range(int(input())):
    N,M,K = list(map(int,input().split()))
    mat = np.zeros((N+1,M+1))
    for i in range(1,N+1):
        temp = list(map(int,input().split()))
        for j in range(1,M+1):
            mat[i][j] = temp[j-1]

    result = 0   
    for i in range(N+1):
        cumSum = 0
        for j in range(M+1):
            mat[i][j] += cumSum
            cumSum = mat[i][j]
            
    for j in range(M+1):
        cumSum = 0
        for i in range(N+1):
            mat[i][j] += cumSum
            cumSum = mat[i][j]
            
    Z = min(N,M)
    for l in range(1,Z+1):
        for i in range(l,N+1):
            for j in range(l,M+1):
                if ((mat[i,j]+mat[i-l,j-l]-mat[i-l,j]-mat[i,j-l])/(l*l)) >= K:
                    result += 1
    # for i2 in range(N):
    #     for j2 in range(M):
    #         for i1 in range(i2+1):
    #             for j1 in range(j2+1):
    #                 if i1-i2 == j1-j2:
    #                     res = mat[i2,j2]
    #                     if i1>0:
    #                         res = res - mat[i1-1,j2]
    #                     if j1 >0:
    #                         res = res - mat[i2,j1-1]
    #                     if i1 > 0 and j1 > 0:
    #                         res += mat[i1-1,j1-1]
    #                     res = res/((i2-i1+1)*(j2-j1+1))
    #                     if res >= K:
    #                         result += 1
                            
    print(result)
    
 

    
    
        
    
