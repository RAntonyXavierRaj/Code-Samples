#Perm missing number
# input = [1,2,3,5,6]
# ans  = 4

def solution(A):
    if len[A]==0:
        return 1
    if len(A) == 1:
        return A[0]-1
    A.sort()
    x = 1
    for i in range(len(A)):
        
        if len(A) == (i+1):
            if A[0]==1:
                return A[-1]+1
            else: 
                return (A[0]-1)
        
        if (A[i]+1) != (A[i+1]):
            x = A[i]+1
            break       
    return x

