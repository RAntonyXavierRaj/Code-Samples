# frog Jump - Your solution
# A frog crosses a road of Y distance, which can jump X every jump, already had crossed D 
How many steps still needed to cross the road  

def solution(X, Y, D):
    count = 0 
    while X < Y:
        count += 1
        X = X + D
    return count

#X=10, Y=85, D=30