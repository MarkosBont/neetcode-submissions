# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0 

        self.numGood = 0

        def dfs(curr, comparison):
            if not curr:
                return 
            
            if curr.val >= comparison:
                self.numGood += 1
                comparison = curr.val
            
            dfs(curr.left, comparison)
            dfs(curr.right, comparison)

        dfs(root, root.val)
        return self.numGood
            


            

