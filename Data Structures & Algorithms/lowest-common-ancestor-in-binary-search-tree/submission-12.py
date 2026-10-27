# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.lowestAncestor = root

        def dfs(curr):
            if curr is None:
                return

            if p.val > curr.val and q.val > curr.val:
                dfs(curr.right)

            elif p.val < curr.val and q.val < curr.val:
                dfs(curr.left)

            else:
                self.lowestAncestor = curr
                return
            
        dfs(root)
        return self.lowestAncestor
        