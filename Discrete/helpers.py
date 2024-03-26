import math


def sum_pos_divisors(integer):
    # S(n) = the sum of all positive divisors of n
    num = 1
    evens = []

    while num <= integer:

        if num % 2 == 0:
            print(num)
            evens.append(num)
        elif num == 1:
            print(num)
            evens.append(num)

        num += 1

    sum = int()

    for i in evens:
        sum += i

    return sum


def find_mod(x):
    # find the modulus of a function
    # function to edit, when needed
    funct = x**3 + 4*x + 3
    final = funct % 5

    return final


if main == __name__:
    # user_inp = int(input("Non-negative integer value: "))
    # print('Answer: ', find_mod(user_inp))

    user_inp = int(input("Non-negative integer value: "))
    print('Answer: ', sum_pos_divisors(user_inp))
