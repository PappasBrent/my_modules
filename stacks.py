#!/usr/bin/python3
'''
Python implementation of stack abstract data type
'''


class Stack:
    '''
    Class for stack data structure. Last in, first out.
    '''

    def __init__(self):
        self.items = []

    def is_empty(self):
        '''
        Returns true if the stack is empty, else returns false
        '''
        return self.items == []

    def peek(self):
        '''
        Returns the element at the top of the stack.
        '''
        return self.items[-1]

    def pop(self):
        '''
        Returns the element at the top of the stack and removes it.
        '''
        return self.items.pop()

    def print_self(self):
        '''
        Prints the contents of the stack
        '''
        print(*self.items[::-1])

    def push(self, val):
        '''
        Adds an element to the stack and returns it.
        '''
        return self.items.append(val)

    def size(self):
        '''
        Returns the size of the stack
        '''
        return len(self.items)


def main():
    '''
    Test
    '''
    stack = Stack()

    for i in range(1, 10):
        stack.push(i)

    stack.print_self()


if __name__ == "__main__":
    main()
