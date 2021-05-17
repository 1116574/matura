def fibonaci_iter(n):
    # idk czy to jest "poprawnie" matematycznie, ale działa kekw
    if n == 1 or n == 2:
        return 1
    
    a = 1
    b = 2
    i = 2

    while True:
        i += 1
        b = a + b
        a = b - a
        # this basically shifts values from a to b from b to void

        if i == n:
            return a


def fibonaci_rek(n):  # w sumie tego nie ma w wymaganiach ale co
    if n == 1 or n == 2:
        return 1
    else:
        return fibonaci_rek(n-1) + fibonaci_rek(n-2)

a = input()
a = int(a)

print(fibonaci_iter(a))
print(fibonaci_rek(a))
