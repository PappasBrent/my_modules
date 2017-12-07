#!/usr/bin/python3
'''
A module containing support for dealing with
tree data structures.
Subtrees are referred to as nodes just for clarification,
though the terms tree and node are really interchangeable.
'''


class BinaryTree:
    '''
    A tree in which each node can only have at max two children
    '''

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

    def total(self):
        '''
        Recursively calculates the sum of the tree's value
        and all of its children's values
        '''
        if self.left is None and self.right is None:
            return self.val
        else:
            return self.val + self.left.total() + self.right.total()


class Tree:
    '''
    A tree in which each node may have any number of children
    '''

    def __init__(self, val, children=None):
        self.val = val
        # This step is neccesary to ensure that an empty list is the
        # default value for the tree's children
        if children is None:
            self.children = []
        else:
            self.children = children

    def __str__(self):
        return str(self.val)

    def total(self):
        '''
        Recursively calculates the sum of the tree's value
        and all of its children's values
        '''
        result = self.val
        if not self.children:
            return result
        else:
            for child in self.children:
                result += child.total()

        return result

    def num_edges(self):
        '''
        Returns the number of edges the tree has
        '''
        result = 0
        if self.children:
            result += len(self.children)
            for child in self.children:
                result += child.num_edges()

        return result

    def num_nodes(self):
        '''
        Returns the total number of nodes under the tree
        '''
        return self.num_edges() + 1

    def add_node(self, parent, child_val):
        '''
        Adds a node to the parent tree. Will search for the
        first node in the parent tree with the value parent
        and then adds a new node with value child_val
        to its children
        '''
        if self.val == parent:
            # Very handy print statement for clarification
            # print("Adding node", child, "to node", self.val)
            self.children.append(Tree(child_val))
        else:
            for child in self.children:
                child.add_node(parent, child_val)

    def remove_node(self, parent, child_val):
        '''
        Removes a tree from the parent node.  Will search for the first node
        in the parent tree with the value parent and then removes node
        with value child from its children
        '''
        if self.val == parent:
            # print("Removing node", child, "from node", self.val)
            for child in self.children:
                if child.val == child_val:
                    self.children.remove(child)
        else:
            for child in self.children:
                child.remove_node(child.val, child_val)

    def check_for_node(self, parent, child_val):
        '''
        Searches a tree for a particular node within it
        '''
        # Print for clarification
        print("Checking", self.val, "for node", (parent, child_val))
        # If the tree's value matches that of the parent,
        # each of its children are checked to be the node
        if self.val == parent:
            if self.children:
                for child in self.children:
                    if child.val == child_val:
                        return True
                # If the loop completes without finding the node,
                # then we can conclude that it is not there at all
                return False
            else:
                return False
        # If the tree is not the parent, then the process is repeated for
        # each of its children (if any)
        else:
            if self.children:
                present = False
                for child in self.children:
                    present = child.check_for_node(parent, child_val)
                    if present:
                        return present
                # If none of the tree's children are the parent of the
                # target node, then we can conclude that
                # this node is a dead-end
                return False
            else:
                return False


def main():
    '''
    Executes script
    '''
    binary_tree = BinaryTree(3, BinaryTree(2), BinaryTree(5))
    print('Binary Tree:', binary_tree.total())

    tree = Tree(1)
    # print('Tree:', tree.total())
    tree.add_node(1, 2)
    # print('Tree:', tree.total())
    tree.add_node(1, 4)
    # print('Tree:', tree.total())

    tree.add_node(2, 3)
    tree.add_node(2, 5)
    tree.add_node(4, 6)
    tree.add_node(6, 7)
    # tree.add_node(7, 8)
    # tree.add_node(7, 9)

    print(tree.total())

    print(tree.check_for_node(7, 9))


if __name__ == "__main__":
    main()
