def f(x): 
    return x**2

def f2(list_x):
    return list(map(lambda x: x**3, list_x))

def cpu_heavy(n,base):
#     import time
#     start = time.time() - base
    count = 0
    for i in range(n):
        count += i
#     stop = time.time() - base
    return count