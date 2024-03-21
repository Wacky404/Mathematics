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
# Truth table is constructioned based on these bool -
# ean values.
#

def operations(i):
    if i == '^':
        pass
    elif i == 'v':
        pass
    elif i == 'V':
        pass
    elif i == '~':
        pass
    # this is a special case, 2 characters
    elif i == '->':
        pass
    # this is a special case, 2 characters
    elif i == '<=>':
        pass
