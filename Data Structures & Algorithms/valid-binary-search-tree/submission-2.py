# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.isValid = True

        def dfs(curr, lowerBound, upperBound):
            if not curr:
                return

            if not lowerBound < curr.val < upperBound:
                self.isValid = False
            
            dfs(curr.left, lowerBound, curr.val)
            dfs(curr.right, curr.val, upperBound)

        
        dfs(root, float('-inf'), float('inf'))

        return self.isValid
        

        