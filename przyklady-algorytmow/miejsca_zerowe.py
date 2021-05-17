# Zakładamy funkcję ciągłą (tj. taką która przybiera wartość dla każdej liczby z przedziału parametrów; nie ma "dziur"; jest pisana nie odrywając ołówka od kartki)
# Zakładamy że funkcja ma jedno miejsce zerowe w przedziale
# src = http://www.algorytm.edu.pl/algorytmy-maturalne/metoda-polowienia-przedzialow.html

import math

def f(x):  # f(2.154) = 0
    return (x**3) - 10

def miejsce(f, min=0, max=5, precision=0.01):
    # osiągnięto minimalną precyzję?
    a = f(min)
    b = f(max)

    if math.fabs(min-max) < precision:
        return (min+max)/2

    # jeśli miejsce zerowe jest na skraju
    if a == 0:
        return min
    elif b == 0:
        return max

    # w większości wypadków:

    if f(min) * f((min+max)/2) < 0:
        # miejsce zerowe znajduje się w lewej połowie
        return miejsce(f, min, (min+max)/2, precision)
    else:
        # miejsce zerowe znajduje się w prawej połowie
        return miejsce(f, (min+max)/2, max, precision)


print(miejsce(f))
# poprawna odpowiedź: 2.154
    
