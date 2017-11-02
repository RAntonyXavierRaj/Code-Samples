#Euclidean algorithm
#Finding GCD

def gcd(x, y):
    if x == y:
        print(x)
        return x
    if x > y:
        gcd(x - y, y)
    else:
        gcd(x, y - x)

#gcd by division
def gcd1(x, y):
    if x % y == 0:
        return y
    else:
        return gcd(y, x % y)