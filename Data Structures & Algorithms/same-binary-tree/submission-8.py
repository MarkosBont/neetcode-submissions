# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.isEquivalent = True

        def dfs(curr_p, curr_q):
            if not curr_p and not curr_q:
                return 
            
            if not curr_p or not curr_q or curr_p.val != curr_q.val:
                self.isEquivalent = False
                return
            
            dfs(curr_p.left, curr_q.left)
            dfs(curr_p.right, curr_q.right)

            return

        dfs(p, q)
        return self.isEquivalent
        