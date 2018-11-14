def fib(n):
    if n in [0, 1]:
        return 1
    elif n % 1 == 0 and n>1:
        return fib(n-2) + fib(n-1)
    else:
        raise ValueError("Needs an integer.")

