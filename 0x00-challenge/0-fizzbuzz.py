#!/usr/bin/python3
# This line ensures the script runs with Python 3

def fizzbuzz(n):
    """
    Prints numbers from 1 to n, replacing multiples of 3 with 'Fizz',
    multiples of 5 with 'Buzz', and multiples of both 3 and 5 with 'FizzBuzz'.
    """
    for i in range(1, n + 1):
        output = ''
        if i % 3 == 0:
            output += 'Fizz'
        if i % 5 == 0:
            output += 'Buzz'
        if output == '':
            output = str(i)
        print(output, end=' ')
    print()


if __name__ == "__main__":
    import sys
    fizzbuzz(int(sys.argv[1]))
