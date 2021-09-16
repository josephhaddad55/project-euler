#!/usr/bin/env python3

# The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143?
def largest_prime_factor(n: int) -> int:
    # The largest divisor to start is 2 because 2 is the smallest prime number
    largest_divisor = 2

    # We divide by the smallest possible number each time until the quotient is equal to 1
    while n % 2 == 0:
        n /= 2

    i = 3
    while n != 1:
        if n % i == 0:
            n /= i
            largest_divisor = i
        # Move on to the next odd number
        i += 2

    return largest_divisor


if __name__ == "__main__":
    assert largest_prime_factor(13195) == 29
    assert largest_prime_factor(600851475143) == 6857
