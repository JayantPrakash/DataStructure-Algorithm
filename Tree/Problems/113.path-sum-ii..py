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
            return []
        
        self.global_box = []
        self.dfs(root, targetSum, [])
        return self.global_box
    
    def dfs(self, node, targetSum, slate):
        slate.append(node.val)
        if node.left is None and node.right is None:
            if targetSum - node.val == 0:
                self.global_box.append(slate[:])

        if node.left is not None:
            self.dfs(node.left, targetSum - node.val, slate)     

        if node.right is not None:
            self.dfs(node.right, targetSum - node.val, slate)    

        slate.pop()

    