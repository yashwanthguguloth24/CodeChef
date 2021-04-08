# Python solution (Partially correct)


# def checkString(main_str,ref_str):
#     flag = False
#     for i in range(len(main_str)--len(ref_str)+1):
#         if main_str[i:i+len(ref_str)] == ref_str:
#             flag = True
#     return flag
# def isSubSequence(string1, string2, m, n):
#     # Base Cases
#     if m == 0:
#         return True
#     if n == 0:
#         return False
#     if string1[m-1] == string2[n-1]:
#         return isSubSequence(string1, string2, m-1, n-1)
#     return isSubSequence(string1, string2, m, n-1)            
def isSubSequence(str1, str2):
    m = len(str1)
    n = len(str2)
 
    j = 0    # Index of str1
    i = 0    # Index of str2
 
    # Traverse both str1 and str2
    # Compare current character of str2 with
    # first unmatched character of str1
    # If matched, then move ahead in str1
 
    while j < m and i < n:
        if str1[j] == str2[i]:
            j = j+1
        i = i + 1
 
    # If all characters of str1 matched,
    # then j is equal to m
    return j == m        


for _ in range(int(input())):
    b_str = input()
    L = len(b_str)
    c_flag = False
    for i in range(2**L):
        bin_val = bin(i)[2:]
        if isSubSequence(bin_val,b_str):
            c_flag = True
        else:
            break
    val = bin(i)[2:]
    print(val)
        
