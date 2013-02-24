#! /usr/bin/env python

class Tree(object):
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
    def sum(self):
        if (self.left is not None and self.right is not None):
            return self.value + max(self.left.sum(), self.right.sum())
        else:
            return self.value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)


def print_tree(tree):
    """
    build set for each level of the tree,
    append to a list and print the list
    """

    tree_list = []
    tree_list_next = [tree]

    i = 0
    while (i != -1):

        tree_list_last = set(tree_list_next)
        tree_list.append(tree_list_last)
        tree_list_next = []

        for t in tree_list_last:
            if (t.left is not None) and (t.right is not None):
                tree_list_next.append(t.left)
                tree_list_next.append(t.right)
            else:
                i = -1

    print tree_list


def read_tree_file():

    f = open("tree_data")
    root = Tree(int(f.readline()))
    prev_line = [root]
    for line in f.readlines():
        left = True
        parent = 0
        next_line = []
        for index, value in enumerate(line.split()):
            length = len(line.split())
            t = Tree(int(value))

            #print index, value, prev_line, parent, prev_line[parent], t
            if (index == 0):
                # first element left only
                prev_line[parent].left = t

            elif (index == length - 1):
                # last element right only
                prev_line[parent].right = t

            else:
                # right element parent
                # left element parent + 1
                prev_line[parent].right = t
                prev_line[parent+1].left = t
                parent = parent + 1

            next_line.append(t)
        prev_line = next_line
    return root

root = read_tree_file()
#print_tree(root)

print root.sum()
