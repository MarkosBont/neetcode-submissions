# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSame(p,q):
            if not p and not q:
                return True
            
            if not p or not q or p.val != q.val:
                return False
            
            return isSame(p.left, q.left) and isSame(p.right, q.right)

        def dfs(curr, subRoot):
            if not subRoot:
                return True
            
            if not curr:
                return False
            
            if isSame(curr, subRoot):
                return True
            
            return dfs(curr.left, subRoot) or dfs(curr.right, subRoot)
        
        return dfs(root, subRoot)


        