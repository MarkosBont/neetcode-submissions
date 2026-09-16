# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        self.goodNodes = 0
        
        def dfs(curr, currMax):
            if not curr:
                return None
            
            if curr.val >= currMax:
                self.goodNodes += 1
                currMax = curr.val
            
            dfs(curr.left, currMax)
            dfs(curr.right, currMax)
        
        dfs(root, -100)
        return self.goodNodes

        
            

            


        