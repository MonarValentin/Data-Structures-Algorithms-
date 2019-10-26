#
#   BST: Binary Search Tree
#
#   BUGS
#
#    Initially I had
#   1.                 if child_tree.item < item: # If less than the item, move to the left
#    I.e. wrong way around. Discovered cos the tree was the wrong order when printed.
#   2. Bug: I initially had str(ptr) instead of str(ptr.item). Very messy.
#
class Node:
    """ A node in a BST. It may have left and right subtrees """
    def __init__(self, item, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right

class BST:
    """ An implementation of a Binary Search Tree """
    def __init__(self):
        self.root = None

    def add(self, item):
        """ Add this item to its correct position on the tree """
        # This is a non recursive add method. A recursive method would be cleaner.
        if self.root == None: # ... Empty tree ...
            self.root = Node(item, None, None) # ... so, make this the root
        else:
            # Find where to put the item
            child_tree = self.root
            while child_tree != None:
                parent = child_tree
                if item < child_tree.item: # If smaller ... 
                    child_tree = child_tree.left # ... move to the left
                else:
                    child_tree = child_tree.right

            # child_tree should be pointing to the new node, but we've gone too far
            # we need to modify the parent nodes
            if item < parent.item:
                parent.left = Node(item, None, None)
            else:
                parent.right = Node(item, None, None)

    # Use count to test.
    def rcount(self, ptr):
        if ptr == None:
            return 0
        else:
            return 1 + self.rcount(ptr.left) + self.rcount(ptr.right)

    def count(self):
        return self.rcount(self.root)

    def rheight(self, ptr):
        if ptr == None:
            return 0
        else:
            return 1 + max(self.rheight(ptr.left), self.rheight(ptr.right))

    def in_order(self, ptr):
        if ptr == None:
            return ""
        else:
            return self.in_order(ptr.left) + str(ptr.item) + "," + self.in_order(ptr.right)

    def __str__(self):
        return self.in_order(self.root)

    def height(self):
        return self.rheight(self.root)

def main():
    lst = [1, 2, 3, 4, 5, 6, 7]
    bst = BST()

    for i in lst:
        bst.add(i)

    print(bst)
    print(bst.count())
    print(bst.height())


    lst = [4, 2, 1, 3, 6, 7, 5]
    bst = BST()

    for i in lst:
        bst.add(i)

    print(bst)
    print(bst.count())
    print(bst.height())

if __name__ == "__main__":
    main()
