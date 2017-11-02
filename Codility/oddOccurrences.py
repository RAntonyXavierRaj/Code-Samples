# Odd occurences in an array
# slower algorithm
# try with A = [1,1,2,2,3]
# expected ans is 3

def solution(A):
    
    y = [int(d) for d in A]
    print (y)
    store = 0
    for i in y:
        count = 0
        for j in range(len(A)):
            if A[j] == i:
                count += 1
        if count%2 != 0:
            store = i
    return (store)

# Odd Occurence
# Faster Algorithm
def solution(A):
    result = 0
    for number in A:
        result = result ^ number
        print (result)
    return result       

        
x = [3,4,3,3,3]
len(x)