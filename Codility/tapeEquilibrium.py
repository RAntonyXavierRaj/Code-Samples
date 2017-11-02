# TapeEquilibrium
# slower algorithm

def solution(A):
    
    if len(A) < 3:
        return abs(A[0]-A[1])
    else:
        val = 2000
        for i in range(1, len(A)):
            x = abs(sum(A[i:])-sum(A[:i]))
            if x < val:
                val = x
        return val

#[-10, -20, -50, -20, 100]