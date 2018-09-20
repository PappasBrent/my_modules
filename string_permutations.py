#!/usr/bin/python3
'''
Practice with string permutations
'''


def permute(s: str):
    '''
    Generates all permutations of a given string

    Args:
        s: The string to permute

    Returns:
        results: A list of the permutations of s
    '''

    if len(s) == 1:
        return [s]
    c = s[0]
    perms = permute(s[1:])
    results = []
    for perm in perms:
        for i in range(len(perm) + 1):
            results.append(perm[:i] + c + perm[i:])
    return results


def main():
    '''
    Executes script
    '''
    print(permute('love'))


if __name__ == "__main__":
    main()
