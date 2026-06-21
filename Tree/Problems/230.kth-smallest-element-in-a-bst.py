from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.nodes_val = []
        self.dfs(root)
        return self.nodes_val[k-1]

    def dfs(self, node):

        if node.left is not None:
            self.dfs(node.left)
        self.nodes_val.append(node.val)

        if node.right is not None:
            self.dfs(node.right)

sol = Solution()
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)     

print(sol.kthSmallest(root,3))                  
                