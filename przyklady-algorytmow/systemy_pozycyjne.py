def konwerter_rekurencyjny(n, base):  # (generator)
    # UWAGA! Zwraca od tyłu, nie tłumaczy na litery (A to 11, B to 12 etc.)
    yield n % base
    if n // base >= base:
        yield from konwerter_rekurencyjny(n // base, base)
    else:
        yield n // base

def konwerter_iteracyjny(n, base):
    # ???
    # nie do końca rozumiem czemu i jak to działa, poprostu tak jakoś mi się dobrze napisało
    result = []
    result.append(n % base)
    while n // base >= base:
        n = n // base
        result.append(n % base)

    result.append(n // base)

    return result


a = 123456
b = 8

print(list(konwerter_rekurencyjny(a, b)))
print(konwerter_iteracyjny(a, b))