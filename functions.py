from unknown_terms.alpha_term import AlphaTerm, MultipleAlphaTerm


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


def compare_alpha_term(term1: AlphaTerm, term2: AlphaTerm):
    if type(term1 * term2) == AlphaTerm and term1.get_exponent() == term2.get_exponent():
        new_term = AlphaTerm(
            term1.get_coefficient() + term2.get_coefficient(),
            term1.get_alpha(),
            term1.get_exponent()
        )
        return new_term
    return None


def compare_multiple_alpha_term(term1: MultipleAlphaTerm, term2: MultipleAlphaTerm):
    if len(term1.terms) == len(term2.terms):
        alphas1 = {t.get_alpha(): t.get_exponent for t in term1.terms}
        alphas2 = {t.get_alpha(): t.get_exponent for t in term2.terms}

        if len(set(alphas1.keys()).union(alphas2.keys())) > len(alphas1):
            return None
        else:
            exp1 = alphas1.values()
            exp2 = alphas2.values()
            if len(set(exp1).union(exp2)) > len(exp1):
                return None
            else:
                return MultipleAlphaTerm(term1.terms + term2.terms)
    else:
        return None
