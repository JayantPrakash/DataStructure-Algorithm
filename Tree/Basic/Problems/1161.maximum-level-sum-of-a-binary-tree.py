# Definition for a binary tree node.
from typing import List, Optional
from collections import deque
from math import inf
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        small_level = 1
        curr_level = 1
        max_sum = -inf
        
        q = deque()
        q.append(root)

        while len(q) != 0:
            len_q = len(q)
            temp = []
            for _ in range(len_q):
                node = q.popleft()
                temp.append(node.val)

                if node.left is not None:
                    q.append(node.left)

                if node.right is not None:
                    q.append(node.right)

            temp_sum = sum(temp)
            if temp_sum > max_sum:
                small_level = curr_level
                max_sum = temp_sum
            curr_level += 1

        return small_level                       
                
sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)     

print(sol.maxLevelSum(root))                  
                
"""
Time and space complexity
T(n) = O(n)
S(n) = O(n)

Pattern - BFS    
                     
Note:

Don't assume max_sum to be 0, assume it to be -inf as all values can be negative in tree

"""   