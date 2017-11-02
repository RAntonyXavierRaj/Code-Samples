# Code for finding binary gap in a number
# input = 9
# answer = 2 (since it has 2 enclosed zeroes)
# input = 5
# anser = 1 (since it has 1 enclosed zero)

def solution(N):  
    count = 0
    store = []
    x = str((bin(N)))
    x = x[2:]
    for i in x:
        if int(i) == 1:
            store.append(count)
            count = 0
            
        if int(i) == 0:
            count += 1  
            
    return max(store)