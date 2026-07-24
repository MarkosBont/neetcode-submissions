# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k_smallest = None
        self.k = k
        self.arr = []

        def dfs(curr):
            if not curr:
                return
            
            dfs(curr.left)
            
            self.arr.append(curr.val)
            if len(self.arr) == self.k:
                self.k_smallest = curr.val
            
            dfs(curr.right)

        dfs(root)
        return self.k_smallest
            
        