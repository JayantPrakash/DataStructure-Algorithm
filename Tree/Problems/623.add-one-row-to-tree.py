# Definition for a binary tree node.
from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:

        if depth == 1:
            new_node = TreeNode(val)
            new_node.left = root
            return new_node
        q = deque()
        q.append(root)
        len_q = len(q)
        curr_depth = 1
        while len(q) != 0:
            len_q = len(q)
            for _ in range(len_q):
                node = q.popleft()

                if node.left is not None:
                    q.append(node.left)

                if node.right is not None:
                    q.append(node.right)

                if curr_depth == depth - 1:
                    new_node_left = TreeNode(val)
                    new_node_right = TreeNode(val)
                    new_node_left.left = node.left
                    new_node_left.right = node.right
                    node.left = new_node_left
                    node.right = new_node_right

                    elif parent.left is node:
                        parent.left = new_node
                        new_node.left = node
                    elif parent.right is node:
                        parent.right = new_node
                        new_node.right = node   

                if depth == max_depth + 1:
                    new_node = TreeNode(val)
                    node.left = new_node
                    node.right = new_node

          
            curr_depth += 1



        return root       

sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)     

print(sol.addOneRow(root, 1, 2))                            

"""
Time and space complexity
T(n) = O(n)
S(n) = O(n)

Pattern - BFS    
"""