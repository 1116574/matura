# def  NWD(a, b):  -- to też by działało
def  NWD_rekursywne(a: int, b: int) -> int:
    remainder = a % b
    if remainder == 0:
        return b
    else:
        a = b
        b = remainder
        return NWD_rekursywne(a, b)


def NWD_iteracyjnie(a: int, b: int) -> int:
    remainder = a % b
    while remainder != 0:
        a = b
        b = remainder
        remainder = a % b
    
    return b


def czynniki_rekursywnie():
    return NotImplementedError

def czynniki_iteracyjnie():
    return NotImplementedError

if __name__ == '__main__':
    # print(NWD_rekursywne(282, 78))
    print(NWD_iteracyjnie(282, 78))

