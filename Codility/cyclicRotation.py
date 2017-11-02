

#CyclicRotation
#For example, given array A = [3, 8, 9, 7, 6] and K = 3, 
#the function should return [9, 7, 6, 3, 8].

def reverse(arr, i, j):
    for idx in range(int((j - i + 1) / 2)):
        arr[i+idx], arr[j-idx] = arr[j-idx], arr[i+idx]
 
def solution(A, K):
    l = len(A)
    if l == 0:
        return []
         
    K = K%l             #excellent point - against double rotation
     
    reverse(A, l - K, l -1)
    #print (A)
    reverse(A, 0, l - K -1)
    #print (A)
    reverse(A, 0, l - 1)
    #print (A)
 
    return A

# Array rotation based on Geeks for Geeks soln (reversing array)
def solution(A, K):
    if len(A) == 0:
        return A
    K = K % len(A)
    X = A[-K:]         # use -K to seperate array dont use K-1
    Y = A[:-K]
    Y.reverse()
    X.reverse()
    A = X + Y
    A.reverse()
    return A
