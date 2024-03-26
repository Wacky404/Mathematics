#
# ====================== Start of Rules of Truth Table Syntax ======================
# A truth table shows how the truth or falsity of a compound statement depends on the
# truth or falsity of the simple statements from which it's constructed.
#
#
# ====================== SYMBOLS ======================
# '^' logical "and" (conjunction)
# 'v' logical "or" (disjunction)
# '~' logical negation
# '->' if left then right
# '<=>' equivalent, if and only if
#
#
# ====================== Logic ======================
# Non-'grammer' symbols will be parsed as variables.
#
# Boolean values of each indivual symbol will get
# assigned a value of False = 0 or True = 1.
#
# Truth table is constructed based on these bool -
# ean values.
#

import parsley
import numpy as np

# TODO: Getting a EOF Error because of parsing error for > in ->


def headers(left, op, right):
    start = str(left)  # .strip('[]').strip("''")
    end = str(right)  # .strip('[]').strip("''")

    operator = op
    # Example: P ^ Q TruthTable
    #  _ _ _ _ _ _ _ _
    # | P | Q | P ^ Q |
    # |- - - - - - - -|
    # | T | T |   T   |
    # |- - - - - - - -|
    # | F | T |   T   |
    # |- - - - - - - -|
    # | T | F |   T   |
    # |- - - - - - - -|
    # | F | F |   F   |
    #  - - - - - - - -
    # False = 0 True = 1

    # This is where I will pass params to generate
    # truth table.
    table_gen(start, operator, end)

    # table = np.array()
    final = f"{start} {operator} {end}"
    return final


def table_gen(exp1, operator, exp2):
    rows = int(11)  # integer going to be replaced by params
    columns = int(17)

    table = np.zeros(shape=(rows, columns), dtype=int)

    length = table[0]
    col = []
    for index, num in enumerate(length):
        col.append(index)

    col = ' '.join(str(e) for e in col)
    print('  ', col)

    for index, r in enumerate(table):
        print(index, r)


# truth table, first build
truthly = parsley.makeGrammar("""

let_num = '('* <letterOrDigit+>:l_n ')'* -> l_n
negation = '~'* ws let_num:n -> str(f'~{n}')
parenthesis = ws '(' negation:x | let_num:x ')' -> x
combo = ws (let_num+:x | negation+:x | parenthesis+:x) -> ''.join(x)
ws = ' '*

table = ws combo:left ws ('^' ws combo:right ws -> headers(left, '^', right)
                     | 'v' ws combo:right ws -> headers(left, 'v', right)
                     | '~' ws combo:right ws -> headers(left, '~', right)
                     | '->' ws combo:right ws -> headers(left, '->', right)
                     | '<=>' ws combo:right ws -> headers(left, '<=>', right)
                     | -> left)

""", {"headers": headers})

# calculator example from docs that we will reference heavily
calc = parsley.makeGrammar("""
# parsley actually has a builtin rule for digit, so you don't have
# to define the rule, you can rely on parsley's builtin rule
# This was the digit rule that was made:
# digit = anything:x ?(x in '0123456789') -> x #
number = <digit+>:ds -> int(ds)
# adding support for whitespace!
ws = ' '*
# This is where we will have the expression to calculate input
expr = number:left ('+' number:right -> left + right
                    | '-' number:right -> left - right
                    | '*' number:right -> left * right
                    | '/' number:right -> left / right
                    | -> left)
""", {})

run = True
while run:

    error = True
    while error:

        try:
            user_input = str(
                input("Input a statement: "))

            error = False

        except Exception as e:
            print(f"An exception of type {type(e).__name__} occurred. "
                  f"Details: Oops... it looks like you didn't input a statement, please try again")

    final_table = truthly(user_input).table()
    print(type(final_table), final_table)

    no_exit = True
    while no_exit:

        try:
            char = str(input('additional expressions?: y/N '))

            if char == 'y':
                no_exit = False

            if char == 'N':
                run = False
                no_exit = False

        except Exception as e:
            print(f"An exception of type {type(e).__name__} occurred. "
                  f"Details: Oops... it looks like you didn't input an character y/N, please try again")
