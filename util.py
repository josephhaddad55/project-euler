#!/usr/bin/env python3

def is_palindrome(n: str) -> bool:
    if n[::-1] == n:
        return True
    return False


def is_prime(n: int) -> bool:
    if n == 1:
        # 1 is not prime
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True
