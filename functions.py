def factoriel(x, min_value=1):
    """ :return x!"""
    counter = 1
    for n in range(min_value, x + 1):
        counter *= n
    return counter


def permutation(n, r):
    return factoriel(n) // factoriel(n - r)


def combination(n, r):
    # return int(permutation(n, r) // factoriel(r))

    min_value = min([n-r, r])
    return factoriel(n, n - min_value + 1) // factoriel(min_value)
