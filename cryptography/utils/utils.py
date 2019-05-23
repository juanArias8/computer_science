from functools import reduce

import sympy.ntheory as nt
from sympy.core.numbers import igcd


def build_prime_number_from_digits_amount(digits_number):
    return nt.nextprime(10 ** digits_number)


def build_random_prime_from_interval(lower_value, higher_value):
    return nt.randprime(lower_value, higher_value)


def get_relative_prime(m, n):
    counter = 3
    while True:
        relative_prime = counter if igcd(counter, m) == 1 else None
        if relative_prime and 2 ** relative_prime > n:
            break
        counter += 1

    return relative_prime


def get_binary_string(number):
    return bin(number)[2:]


def get_number_powers_from_exponent(base, binary_exponent, module):
    list_powers = [base % module]
    for i in range(1, len(binary_exponent)):
        list_powers.append(((list_powers[-1]) ** 2) % module)
    return list_powers


def get_powers_in_module(base, exponent, module):
    binary_base = get_binary_string(exponent)
    bin_len = len(binary_base)
    list_powers = get_number_powers_from_exponent(base, binary_base, module)
    selected_powers = [list_powers[i] for i in range(bin_len) if
                       binary_base[bin_len - 1 - i] == '1']
    product_selected_powers = reduce(lambda a, b: a * b, selected_powers)

    return product_selected_powers % module


def get_exponent_for_decrypt(module):
    nt.totient(module) - 1


if __name__ == '__main__':
    first_number = build_prime_number_from_digits_amount(10)
    second_number = build_random_prime_from_interval(
        10 ** (len(str(first_number)) * 2), 10 ** (len(str(first_number)) * 3)
    )
    print(first_number)
    print(second_number)
    print(get_binary_string(20))
    print(get_powers_in_module(7, 91, 100))
