# Factorisation
# Code for finding the factors of a number
def arrayF(n):
    F = [0] * (n + 1)
    i=2
    while(i * i <= n):
        if (F[i] == 0):
            k=i * i
            while (k <= n):
                if (F[k] == 0):
                    F[k] = i;
                k += i
        i += 1
    return F
    
def factorization(x, F):     ##This function just returns if it is prime
    primeFactors = []
    while (F[x] > 0):
        primeFactors += [F[x]]
        x /= F[x]
    primeFactors += [x]
    return primeFactors





