#!/usr/bin/python3
"""FizzBuzz"""

import sys
import argparse


def fizzbuzz(n):
    """
    FizzBuzz function prints numbers from 1 to n separated by a space.
    For multiples of three print "Fizz" instead of the number and for
    multiples of five print "Buzz".
    For numbers which are multiples of both three and five print "FizzBuzz".
    Args:
    n (int): The upper limit for the FizzBuzz sequence.
    Returns: None
    """
    if n < 1:
        return

    tmp_result = []
    for i in range(1, n + 1):
        if i % FIZZ == 0 and i % BUZZ == 0:
            tmp_result.append("FizzBuzz")
        elif i % FIZZ == 0:
            tmp_result.append("Fizz")
        elif i % BUZZ == 0:
            tmp_result.append("Buzz")
        else:
            tmp_result.append(str(i))
    print(" ".join(tmp_result))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="FizzBuzz")
    parser.add_argument(
            "number", type=int, help="Upper limit for FizzBuzz sequence")
    args = parser.parse_args()

    FIZZ = 3  # Constant for multiples of 3
    BUZZ = 5  # Constant for multiples of 5

    fizzbuzz(args.number)
