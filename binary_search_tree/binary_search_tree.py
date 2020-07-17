"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)     

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target >= self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False
        else:
            if self.left:
                return self.left.contains(target)
            else:
                return False 

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.right:
            self.right.for_each(fn)

        if self.left:
            self.left.for_each(fn)

    def iterative_depth_first_for_each(self, fn):
        # DFT: LIFO 
        # we'll use a stack 
        stack = []
        stack.append(self)

        # so long as our stack has nodes in it
        # there's more nodes to traverse
        while len(stack) > 0:
            # pop the top node from the stack 
            current = stack.pop()

            # add the current node's right child first 
            if current.right:
                stack.append(current.right)

            # add the current node's left child 
            if current.left:
                stack.append(current.left)

            # call the anonymous function 
            fn(current.value)

    # def iterative_breadth_first_for_each(self, fn):
    #     from collections import deque

    #     # BFT: FIFO 
    #     # we'll use a queue to facilitate the ordering 
    #     queue = deque()
    #     queue.append(self)

    #     # continue to traverse so long as there are nodes in the queue
    #     while len(queue) > 0:
    #         current = queue.popleft()

    #         if current.left:
    #             queue.append(current.left)

    #         if current.right:
    #             queue.append(current.right)

    #         fn(current.value)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            node.left.in_order_print(node.left)
        print(node.value)
        if node.right:
            node.right.in_order_print(node.right)


        # newList = []
        # newList.append(self.value)
        
        
        # if self.left :
        #     self.left.in_order_print(node)

        # if self.right:
        #     self.right.in_order_print(node)

        # flatList = [val for sublist in newList for val in sublist]

        # print(f"{flatList}")



    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        from collections import deque

        queue = deque()
        queue.append(node)

        # continue to traverse so long as there are nodes in the queue
        while len(queue) > 0:
            current = queue.popleft()

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

            print(current.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = []
        stack.append(node)

        while len(stack) > 0:
            current = stack.pop()

            if current.right:
                stack.append(current.right)

            if current.left:
                stack.append(current.left)

            print(current.value)

        

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    
    def pre_order_dft(self, node):
        print(node.value)
        if node.left:
            node.left.pre_order_dft(node.left)

        if node.right:
            node.right.pre_order_dft(node.right)


    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left:
            node.left.post_order_dft(node.left)

        if node.right:
            node.right.post_order_dft(node.right)
        
        print(node.value)
