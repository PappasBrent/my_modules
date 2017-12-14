#!/usr/bin/python3
'''
A module containing examples of different types of sorting methods
'''


def insertion_sort(arr):
    '''
    Insertion sort
    '''

    # Begins the checking at the beginning of the array
    for i in range(1, len(arr)):
        # Stores the current value at i if it will be needed
        start = arr[i]
        # Sets the value of j to one less than i. This is so that
        # j will reference the item at index i - 1 (the item before i)
        j = i - 1
        # Runs while j refers directly to an item beyond the first one
        # in the array and the item at j is bigger than the item at i
        # (while the item before the item at i is bigger than the item at i)
        while j >= 0 and arr[j] > start:
            '''
            Sets the value ahead of the item at j (the item at i)
            to be the item at j (shifts the item at j forward in the list).
            Note that when this finishes the item directly after the item at
            index j will be a duplicate of the item at j, and not the value of
            the item originally at the index i as it should be.
            This is accounted for.
            '''
            arr[j + 1] = arr[j]
            # Shift j back one place in the array, so that the item behind
            # j gets moved foward next.
            j -= 1
        # Accounts for the issue mentioned above
        arr[j + 1] = start
        # Animated example of the array in action:
        # https://upload.wikimedia.org/wikipedia/commons/9/9c/Insertion-sort-example.gif


def main():
    '''
    Executes script
    '''
    pass


if __name__ == "__main__":
    main()
