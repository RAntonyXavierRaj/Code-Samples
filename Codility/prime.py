#Finding prime number - LAMBERT    
    
def isPrime(n):
    for i in range(2, n):
        if n % i == 0 :
            return [False, n]
        else: 
            continue
    return [True, n]
        

x = [isPrime(j) for j in range(2, 51)]
print (x)      
      