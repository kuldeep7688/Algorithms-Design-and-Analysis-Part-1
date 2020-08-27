class Node(object):
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.parent = None

    def __str__(self):
        return str(self.data)


class BinarySearchTree(object):
    def __init__(self, root):
        self.root = root
        self.size = 1

    def insert(self, node):
        current_node = self.root
        prev_node = None
        while current_node:
            if node.data < current_node.data:
                prev_node = current_node
                current_node = current_node.left_child
            else:
                prev_node = current_node
                current_node = current_node.right_child

        if node.data < prev_node.data:
            prev_node.left_child = node
            node.parent = prev_node
        else:
            prev_node.right_child = node
            node.parent = prev_node
        self.size += 1
        return

    def search(self, data):
        current_node = self.root
        key_found = False
        while current_node and key_found is False:
            if data == current_node.data:
                key_found = True
            elif data < current_node.data:
                current_node = current_node.left_child
            elif data > current_node.data:
                current_node = current_node.right_child

        return key_found

    def find_minimum_key(self):
        current_node = self.root

        while current_node.left_child is not None:
            current_node = current_node.left_child
        return current_node.data

    def find_predecessor_of_give_key(self, key):
        # finding the key
        predecessor_key = "No key found"
        current_node = self.root
        key_found = False
        while key_found is False:
            if key < current_node.data:
                current_node = current_node.left_child
            elif key > current_node.data:
                current_node = current_node.right_child
            else:
                key_found = True

        # then finding predecessor
        if current_node.left_child is not None:
            # find the right most value
            current_node = current_node.left_child
            while current_node.right_child:
                current_node = current_node.right_child
            predecessor_key = current_node.data
        else:
            # go to parents and return the first value less than key
            current_parent = current_node.parent
            while current_parent and current_parent.data > key:
                current_parent = current_parent.parent
            if current_parent:
                predecessor_key = current_parent.data
        return predecessor_key


def in_order_tree_traversal(root_of_tree):
    if root_of_tree:
        if root_of_tree.left_child:
            in_order_tree_traversal(root_of_tree.left_child)
        print(root_of_tree.data)

        if root_of_tree.right_child:
            in_order_tree_traversal(root_of_tree.right_child)
    else:
        return


if __name__ == "__main__":
    r = Node(7)
    bst = BinarySearchTree(r)

    bst.insert(Node(7))
    bst.insert(Node(1))
    bst.insert(Node(5))

    bst.insert(Node(17))
    bst.insert(Node(11))
    bst.insert(Node(2))
    print("The Minimum key in the Tree is {}".format(bst.find_minimum_key()))
    print("The Predecessor of key 17 in the Tree is {}".format(bst.find_predecessor_of_give_key(17)))
    print("Is 2 present in Tree : {}".format(bst.search(2)))
    print("In Order Traversal of the ")
    in_order_tree_traversal(bst.root)
