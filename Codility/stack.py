# a simple stack data structure implementation.

queue = [0] * N
head, tail = 0, 0
def push(x):
    global tail
    tail = (tail + 1) % N
    queue[tail] = x
def pop():
    global head
    head = (head + 1) % N
    return queue[head]
def size():
    return (tail - head + N) % N
def empty():
    return head == tail