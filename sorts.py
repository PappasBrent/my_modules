#!/usr/bin/python3
'''
A module containing examples of different types of sorting methods
'''


def swap(arr, i, j):
    '''
    Swaps two elements in an array at the given indices
    '''
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def bubble_sort(arr):
    '''
    Bubble sort
    '''

    is_sorted = False
    last_unsorted = len(arr)

    while not is_sorted:
        is_sorted = True
        for i in range(last_unsorted - 1):
            if arr[i + 1] < arr[i]:
                swap(arr, i, i + 1)
                is_sorted = False
        last_unsorted -= 1


def selection_sort(arr):
    '''
    Selection sort
    '''

    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        swap(arr, i, min_index)


def insertion_sort(arr):
    '''
    Insertion sort
    Animated example of the sort in action:
    https://upload.wikimedia.org/wikipedia/commons/9/9c/Insertion-sort-example.gif
    '''

    for i in range(1, len(arr)):
        j = i
        while j >= 1 and arr[j] < arr[j - 1]:
            swap(arr, j, j - 1)
            j -= 1


def main():
    '''
    Executes script
    '''
    nums = [x for x in range(25, 0, -1)]
    print(*nums)
    bubble_sort(nums)
    # selection_sort(nums)
    # insertion_sort(nums)
    print(*nums)


if __name__ == "__main__":
    main()
