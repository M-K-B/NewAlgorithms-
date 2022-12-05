""" Basic BST code for inserting (i.e. building) and printing a tree

    Your ***first standard viva task*** (of 5) will be to implement a find method into
    the class BinaryTree from pseudocode. See the lab task sheet for Week 4. 

    Your ***first advanced viva task*** (of 3) will be to implement a remove (delete) method
    into the class Binary Tree from partial pseudocode. See the lab task sheet for Week 4.

    Since the given code is in python it is strongly suggested you stay with python; but
    if you want to reimplement as C++ this is also OK (but not worth extra credit)
"""

import math

""" Node class
"""

class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

""" BST class with insert and display methods. display pretty prints the tree
"""

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)
        else:
            print("Value already present in tree")






    def display(self, cur_node):
        lines, _, _, _ = self._display(cur_node)
        for line in lines:
            print(line)

    def _display(self, cur_node):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if cur_node.right is None and cur_node.left is None:
            line = '%s' % cur_node.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if cur_node.right is None:
            lines, n, p, x = self._display(cur_node.left)
            s = '%s' % cur_node.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if cur_node.left is None:
            lines, n, p, x = self._display(cur_node.right)
            s = '%s' % cur_node.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self._display(cur_node.left)
        right, m, q, y = self._display(cur_node.right)
        s = '%s' % cur_node.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


    def find_i(self, target):    # define function find i (find interativly ) with self and target as parameters 
        cur_node = self.root    # self.root is assigned to current node
        while cur_node != None: # while current node is not None 
            if cur_node.data == target:  # if the data in current node is eqaul to target 
                return True                 # return True
            elif cur_node.data > target:  # if the data in  current node is greater than target 
                cur_node = cur_node.left  # current left is assigned to current node 
            else:
                cur_node = cur_node.right # else current node right is assigned to current node 
        return False # return false 

    ''''''
    def find_r(self, target):  # define function find r (recursively ) with self and target as parameters 
        if self.root:                 # checks self.root                         
            if self._find_r(target,self.root): # if self recurrsive function with target and root 
                return True  # return True
            return False # return False 
        else:
            return None # else None
    
    def _find_r(self, target, cur_node): # defins function  with self, target , current node (curr_node)
        if target > cur_node.data and cur_node.right: # if target is greater than current node data and current node right 
            return self._find_r(target, cur_node.right) # return and call the function self . find R with right 
        elif target < cur_node.data and cur_node.left: # if target is less than current node data  and left node 
            return self._find_r(target, cur_node.left) # return and call the function self . find R with left 
        if target == cur_node.data:  # if target is equal to current node
            return True # return True

    def remove(self, target): # def remove function with self and target as parameters 
        if self.root is None: # if self.root is None then return False
            return False
        elif self.root.data == target: # else if self root data is equal to target proceed 
            if self.root.left is None and self.root.right is None: # if self root left is none and self root right is none 
                self.root = None # assign none to self root 
            elif self.root.left and self.root.right is None: # else if self root left and self root right is None 
                self.root = self.root.left # assign left to self root 
            elif self.root.left is None and self.root.right:# else if self root left None and self root right  
                self.root = self.root.right  # assign right to self root 
            elif self.root.left and self.root.right: # else if self root left and self root right  
                delNodeParent = self.root # delete Node parent = self.root
                delNode = self.root.right # delete Node = self root right 

                while delNode.left: # while delete Node left 
                    delNodeParent = delNode # assign delete node to delete node parent 
                    delNode = delNode.left # assign delete node to delete node 

                self.root.data = delNode.data # assign delete node data to self root data 
                if delNode.right:  # if delete node right 
                        if delNodeParent.data > delNode.data: # if delete node parent data is greater than delete node data 
                            delNodeParent.left = delNode.right # assign delete node right to delete node parent left
                        elif delNodeParent.data < delNode.data: # else if delete node data less than delete node data 
                            delNodeParent.right = delNode.right # assign delete node right to delete node parent
                else:
                    delNodeParent.right = None # else assign none to delete node parent right 
        parent = None # set parent to None 
        node = self.root # set node to self root 

        while node and node.data != target: # while node and node data are not target 
            parent = node # set parent to node 
            if target < node.data: # if target is less than node data 
                node = node.left # node left is assigned to node 
            elif target > node.data: # else if target is greater than node data 
                node = node.right # node right is assigned to node 

        if node is None or node.data != target: # if node is none  or node data is not target 
            return False # retunr false 

        elif node.left is None and node.right is None: # else if node left is none and node right is none 
            if target < parent.data: # if target is less than parent data 
                parent.left = None # parent left is set to none 
            else:
                parent.right = None # else parent right is set to none
            return True # return True 

        elif node.left and node.right is None: # else if node left and node right is None
            if target < parent.data: # if target is less than parent data
                parent.left = node.left #node left is assigned to parent left 
            else:
                parent.right = node.left # else node left is assigned to parent right 
            return True
        
        else: 
            delNodeParent = node # delete node parent is assigned node 
            delNode = node.right # delete node is assigned node right 
            while delNode.left: # while delete node left 
                delNodeParent = delNode  # delete node parent is assigned delete node 
                delNode = delNode.left  # delete node is assigned delete node left 
            
            node.data = delNode.data  # node data is set to delete node data 
            if delNode.right: # delete node right 
                if delNodeParent.data > delNode.data: # if delete node parent data is greater than delete node data 
                    delNodeParent.left = delNode.right # delete node parent left is assigned delete node right 
                elif delNodeParent < delNode.data: # delete node parent less than delete node data 
                    delNodeParent.right = delNode.right # delete node parent right is assigned delete node right 
            else:
                if delNode.data < delNodeParent.data: # else  delete node data less than parent data 
                    delNodeParent.left = None # delete parent left is none
                else:
                    delNodeParent.right = None  # delete parent right is none

        
bst = BinaryTree()
bst.insert(4)
bst.insert(2)
bst.insert(6)
bst.insert(1)
bst.insert(3)
bst.insert(5)
bst.insert(7)

##bst.insert(8)
##bst.insert(9)
##bst.insert(10)
##bst.insert(11)
##bst.insert(12)
##bst.insert(13)
##bst.insert(14)
##bst.insert(15)
##bst.insert(100)
##bst.insert(200)


bst.display(bst.root)



print(bst.find_i(3))
print(bst.find_r(3))

print(bst.remove(3))

bst.display(bst.root)
