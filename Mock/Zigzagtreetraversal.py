# Definition for a binary tree node.
from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []

        q = deque()
        q.append(root)
        result = []
        flag = True
        while(len(q) != 0):
            num_nodes = len(q)
            temp = []
            for _ in range(num_nodes):
                node = q.popleft()
                temp.append(node.val)
                if node.left is not None:
                    q.append(node.left)

                if node.right is not None:
                    q.append(node.right)

            if flag:
                flag = False
            else:    
                temp.reverse()
                flag = True   

            result.append(temp)             

        return result
    
sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)     

print(sol.zigzagLevelOrder(root))        

                
#T(n) = O(n)
#S(n) = O(n)                