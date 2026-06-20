from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.isValid = True
        self.dfs(root)
        return self.isValid
    
    def dfs(self,node):

        if node.left is None and node.right is None:
            return True
        
        is_local_bst = True
        if node.left is not None:
            is_left_valid = self.dfs(node.left)
            
            if not is_left_valid or node.val <= node.left.val:
                self.isValid = False
                is_local_bst = False

        if node.right is not None:
            is_right_valid = self.dfs(node.right)
            
            if not is_right_valid and node.val >= node.right.val:
                self.isValid = False
                is_local_bst = False

        return is_local_bst        


sol = Solution()
root = TreeNode(2)
root.left = TreeNode(2)
root.right = TreeNode(2)
#root.left.left = TreeNode(4)
#root.left.right = TreeNode(5)
#root.right.right = TreeNode(6)     

print(sol.isValidBST(root))           

        