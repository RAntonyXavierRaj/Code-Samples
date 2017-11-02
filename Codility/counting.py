# Code for counters and finding prefix_sums

#maxCounters
def solution(N, A):
    counter = [0] * N
    for i in range(len(A)):
        if 1 <= A[i] <= N:
            counter[A[i]-1] += 1
        elif A[i] == N+1:
            x = max(counter)
            counter = [x] * N
    return counter


def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P







