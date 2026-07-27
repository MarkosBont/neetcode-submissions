# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.goodNodes = 0

        def dfs(curr, lowerBound):
            if not curr:
                return
            
            if curr.val >= lowerBound:
                self.goodNodes += 1
                lowerBound = curr.val
            
            
            
            dfs(curr.left, lowerBound)
            dfs(curr.right, lowerBound)
        

        dfs(root, root.val)
        return self.goodNodes