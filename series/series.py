
def fibonacci(n):
    if n >= 2:
        return fibonacci(n - 2) + fibonacci(n - 1)
    return n
    


def lucas(n):
    if n == 0:
        return n+2
    elif n == 1:
        return n
    elif n >= 2:
        return lucas(n - 2) + lucas(n - 1)
    return n


def sum_series(n, optional1=0, optional2=1):
    if n == 0:
        i=0
        return optional1
    elif n == 1:
        return optional2
    elif n >= 2:
        return sum_series(n - 2) + sum_series(n - 1)
    return n

fibonacci(2)
# sum_series(n)
