# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiameter = 0

        def dfs(curr):
            if curr is None:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)

            self.maxDiameter = max(self.maxDiameter, left + right)

            return 1 + max(left, right)

        dfs(root)

        return self.maxDiameter
        