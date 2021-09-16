#!/usr/bin/env python3
from util import is_palindrome


# A palindromic number reads the same both ways. The largest palindromic made from the product of two digit numbers is
# 9009 = 91 x 99. Find the largest palindrome made from the product of two 3-digit numbers.

def largest_palindrome_product(number_of_digits: int) -> int:
    largest_palindrome = 0

    start_value_string = "1"
    for i in range(1, number_of_digits):
        start_value_string += "0"

    finish_value_string = start_value_string + "0"
    start_value = int(start_value_string)
    finish_value = int(finish_value_string)

    print(f"Range of values is between {start_value} - {finish_value}")

    for i in range(start_value, finish_value):
        for j in range(start_value + 1, finish_value):
            product = i * j
            if is_palindrome(str(product)) and product > largest_palindrome:
                largest_palindrome = product

    return largest_palindrome


if __name__ == "__main__":
    assert largest_palindrome_product(2) == 9009
    assert largest_palindrome_product(3) == 906609
