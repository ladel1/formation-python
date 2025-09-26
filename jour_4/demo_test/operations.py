def caree(n: int) -> int:
    if(n == 5):
        return n
    return n ** 2

def div(a: int, q: int) -> float:
    try:
        return a / q
    except ZeroDivisionError:
        raise Exception("infinity")

def factorielle(n: int):
    """
    0! = 1
    1! = 1
    2! = 1 * 2 = 2
    3! = 1 * 2 * 3 = 6
    4! = 1 * 2 * 3 * 4 = 24
    5! = 1 * 2 * 3 * 4 * 5 = 120 
    """
    f = 1
    for i in range(1,n+1):
        f = f * i
    return f