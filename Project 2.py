class TernaryTree(object):
    def __init__(self, value=None):
        self.value = value
        self.right = None
        self.left = None
        self.middle = None

    def insert_node(self, new_value):
        if new_value < self.value:
            if self.left is None:
                self.left = TernaryTree(new_value)
            else:
                self.left.insert_node(new_value)
        elif new_value == self.value:
            if self.middle is None:
                self.middle = TernaryTree(new_value)
        else:
            if self.right is None:
                self.right = TernaryTree(new_value)
            else:
                self.right.insert_node(new_value)

    def generate_tree(self, L):
        self.value = L[0]
        for i in L[1:]:
            self.insert_node(i)

    def traverse_WLMR(self):
        if self is None:
            return
        print(self.value)
        TernaryTree.traverse_WLMR(self.left)
        TernaryTree.traverse_WLMR(self.middle)
        TernaryTree.traverse_WLMR(self.right)

    def non_leaf_count(self):
        if self is None:
            return 0

        nonleafcounter = 0

        a = self.left
        b = self.middle
        c = self.right

        if (a is not None) or (b is not None) or (c is not None):
            nonleafcounter += 1

        # recursively checks each leaf
        nonleafcounter += TernaryTree.non_leaf_count(a)

        nonleafcounter += TernaryTree.non_leaf_count(b)

        nonleafcounter += TernaryTree.non_leaf_count(c)

        return nonleafcounter

    def leaf_count(self):
        if self is None:
            return 0

        if self.left is None and self.right is None and self.middle is None:
            return 1

        countLeaf = 0
        countLeaf += TernaryTree.leaf_count(self.left)
        countLeaf += TernaryTree.leaf_count(self.middle)
        countLeaf += TernaryTree.leaf_count(self.right)
        return countLeaf

    def degree_two_nodes_count(self):
        if self is None:
            return 0
        twonodescounter = 0
        if (self.left is None) and (self.middle is not None) and (self.right is not None):
            twonodescounter += 1
        elif (self.left is not None) and (self.middle is None) and (self.right is not None):
            twonodescounter += 1
        elif (self.left is not None) and (self.middle is not None) and (self.right is None):
            twonodescounter += 1

        twonodescounter += TernaryTree.degree_two_nodes_count(self.left)
        twonodescounter += TernaryTree.degree_two_nodes_count(self.middle)
        twonodescounter += TernaryTree.degree_two_nodes_count(self.right)
        return twonodescounter

    def tree_depth(self):
        if self is None:
            return 0

        if (self.left is None) and (self.middle is None) and (self.right is None):
            return 0

        else:
            return max(TernaryTree.tree_depth(self.left) + 1, TernaryTree.tree_depth(self.middle) + 1, TernaryTree.tree_depth(self.right) + 1)


def main():
    L = [4, 1, 2, 2, 3, 1, 0, 4, 6, 5, 6, 4]
    T = TernaryTree()
    T.generate_tree(L)
    T.traverse_WLMR())
    T.non_leaf_count())
    T.leaf_count())
    T.degree_two_nodes_count())
    T.tree_depth())


main()