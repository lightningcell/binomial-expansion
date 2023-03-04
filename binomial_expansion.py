from functions import *
from unknown_terms.alpha_term import *


def binomial_expansion(term1, term2, exponent) -> str:
    """:return (term1 + term2) ^^ exponent"""

    is_exponent_negative = exponent < 0
    term_counter = abs(exponent) + 1
    equation = ""

    if type(term1) == type(term2):
        if type(term1) == AlphaTerm:
            compare = compare_alpha_term(term1, term2)
            if compare:
                return TermPrinter.print(compare ** exponent, True, 0)
        elif type(term1) == MultipleAlphaTerm:
            compare = compare_multiple_alpha_term(term1, term2)
            if compare:
                return TermPrinter.print(compare ** exponent, True, 0)
        else:
            return str((term1 + term2) ** exponent)

    for i in range(0, term_counter):
        comb = combination(abs(exponent), i)
        tx = term1 ** (abs(exponent) - i)
        ty = term2 ** i
        main_term = comb * tx * ty

        if (i == 0 and main_term.get_coefficient() > 0) or main_term.get_coefficient() == 0:
            with_sign = False
        else:
            with_sign = True

        equation += TermPrinter.print(main_term, with_sign, 1)

    if not is_exponent_negative:
        return equation.strip()
    else:
        return f"({equation.strip()}){TermPrinter.get_printable_exponent(-1, False)}"
