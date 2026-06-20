# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        self.count_good_nodes = 0

        self.dfs(root, slate = [])

        return self.count_good_nodes
    
    def dfs(self, node, slate):
        slate.append(node.val)

        if node.left is not None:
            self.dfs(node.left, slate)

        if node.right is not None:
            self.dfs(node.right, slate)

        if node.val >= max(slate):
            self.count_good_nodes += 1

        slate.pop()            

sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)     

print(sol.goodNodes(root))           