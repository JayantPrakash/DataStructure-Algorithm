# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """

        if root is None:
            return False
        
        self.global_box = False
        self.dfs(root, targetSum)
        return self.global_box
    
    def dfs(self, node, targetSum):

        if node.left is None and node.right is None:
            if targetSum - node.val == 0:
                self.global_box = True

        if node.left is not None:
            self.dfs(node.left, targetSum - node.val)     

        if node.right is not None:
            self.dfs(node.right, targetSum - node.val)    

    

    