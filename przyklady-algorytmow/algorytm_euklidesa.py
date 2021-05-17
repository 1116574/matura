# def  NWD(a, b):  -- to też by działało
def  NWD_rekurencyjnie(a: int, b: int) -> int:
    remainder = a % b
    if remainder == 0:
        return b
    else:
        a = b
        b = remainder
        return NWD_rekurencyjnie(a, b)


def NWD_iteracyjnie(a: int, b: int) -> int:
    remainder = a % b
    while remainder != 0:
        a = b
        b = remainder
        remainder = a % b
    
    return b


def czynniki_rekurencyjnie(n, k=2):
    return NotImplementedError
    if n % k == 0:
        yield k
        yield from czynniki_rekurencyjnie(n//k, k)
    else:
        yield from czynniki_rekurencyjnie(n//k, k+1)

def czynniki_iteracyjnie(n):
    # src = https://maturka.it/algorytmy/python-rozklad-liczby-na-czynniki-pierwsze/
    czynniki = []
    k = 2
    while n != 1:
        while n % k == 0:
            n //= k
            czynniki.append(k)
        k += 1
    
    return czynniki

if __name__ == '__main__':
    print(NWD_rekurencyjnie(282, 78))
    print(NWD_iteracyjnie(282, 78))
    print(czynniki_iteracyjnie(212))
    print(list(czynniki_rekurencyjnie(6)))


