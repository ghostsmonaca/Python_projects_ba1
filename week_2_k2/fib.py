def fib(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fib(n-1) + fib(n-2) 

def fib2(n, d = 0):
    print(f"fib({n}, {d})")
    if n == 1:
        print("return 1")
        return 1
    elif n == 0:
        print("return 0")
        return 0
    else:
        d = d + 1
        return fib2(n-1, d) + fib2(n-2, d)
    
fib2(5,0)