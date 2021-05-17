def dzielniki(n):
    result = []
    k = 1

    while n >= k:
        if n % k == 0:
            result.append(k)
        k += 1
    
    return result


def doskonala(n, dzielniki):
    dzielniki.remove(n)
    if sum(dzielniki) == n:
        return True
    else:
        return False

def pierwsza(n):
    if len(dzielniki(n)) == 2:
        return True
    else:
        return False



a = input()
a = int(a)
print(dzielniki(a))
print(doskonala(a, dzielniki(a)))
print(pierwsza(a))
