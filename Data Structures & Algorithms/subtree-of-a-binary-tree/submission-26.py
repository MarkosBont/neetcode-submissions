# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.exists = False

        def isSameTree(p, q):
            if not p and not q:
                return True
        
            if not p or not q or q.val != p.val:
                return False

            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        def dfs(curr):
            if not curr:
                return

            if isSameTree(curr, subRoot):
                self.exists = True
                return
            
            else:
                dfs(curr.left)
                dfs(curr.right)

            return
        

        dfs(root)
        return self.exists

