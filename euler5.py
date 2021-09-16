#!/usr/bin/env python3
from typing import List


def remove_multiples_from_list(arr: List[int]) -> List[int]:
    """
    Removes lesser multiples of an sequential ascending array
    :param arr: Sequentially ascending list of integers
    :return: List of numbers who have no common multiples within the array
    """

    for i in reversed(arr):
        if i == 1:
            # Everything is a multiple of 1 so pass to the next iteration
            pass
        for j in range(2, i):
            if i % j == 0:
                arr.remove(j)
    return arr


# 2520 is the smallest number that can be divided by each of the numbers from 1 t0 10 without any remainder. What is
# the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
def smallest_number_divisible_by(largest_divisor: int) -> int:
    result = None
    unsolved = True
    potential_solution = largest_divisor
    divisors = list(range(2, largest_divisor + 1))

    # remove multiple from list of divisors. e.g. if a number is divisible by 20 is also divisible by 2, therefore
    # we don't need to check if the number is divisible by 20
    divisors = remove_multiples_from_list(divisors)

    while unsolved:
        # check if that number is divisible by all divisors
        for divisor in divisors:
            if potential_solution % divisor != 0:
                # Break out of the inner loop and move onto the next number
                break
            if divisor == largest_divisor:
                # We found the smallest product
                result = potential_solution
                unsolved = False

        potential_solution += largest_divisor

    return result


if __name__ == "__main__":
    assert smallest_number_divisible_by(largest_divisor=20) == 232792560
