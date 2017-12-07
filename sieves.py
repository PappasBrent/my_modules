#!/usr/bin/python3
'''
Module containing different types of sieves
'''


def get_primes_sieve_eratosthenes(num):
    '''
    Returns a list of all prime numbers from 0 to num (inclusive)
    Info:
    https://iamrafiul.wordpress.com/2013/04/28/sieve-of-eratosthenes-in-python/
    '''
    # List of composite numbers
    composites = []
    # List of prime numbers
    primes = []
    # Begins counting at 2, the first prime number
    for i in range(2, num + 1):
        # Checks if the number is in the list composites
        if i not in composites:
            # If not, then it is added to the list of primes
            primes.append(i)
            # Then, every integer from the the square of
            # i up to an including n that is a multiple of i
            # is added to the list of composites (since
            # they are all evenly divisible by i)
            for j in range(i**2, num + 1, i):
                composites.append(j)
    # Returns the list of primes
    return primes


def main():
    '''
    Executes script
    '''
    print(*get_primes_sieve_eratosthenes(10000))


if __name__ == "__main__":
    main()
