#!/usr/bin/python3
'''
A class for the Python implementation of queues
'''


class Node:
    '''
    A class for nodes in a linked list
    '''

    def __init__(self, val=None, following=None):
        self.val = val
        self.next = following


class Queue:
    '''
    A class for queues
    '''

    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        '''
        Appends a new value to the end of the queue
        '''
        new = Node(val)
        if self.head is None:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new

    def remove(self):
        '''
        Deletes a value from the front of the queue
        '''
        temp = self.head
        self.head = self.head.next

        del temp

    def print_self(self):
        '''
        Prints the contents of the queue
        '''
        temp = self.head
        while temp is not None:
            print(temp.val, end='<-')
            temp = temp.next
        print('None')


def main():
    '''
    Executes script
    '''
    q = Queue()

    q.insert(5)
    q.insert(4)
    q.insert(3)
    q.print_self()
    q.remove()
    q.print_self()


if __name__ == "__main__":
    main()
