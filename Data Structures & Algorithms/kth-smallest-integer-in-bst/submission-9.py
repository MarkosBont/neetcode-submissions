# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k_smallest = None
        self.counter = 0

        def dfs(curr, k):
            if not curr:
                return
            
            dfs(curr.left, k)
            
            self.counter += 1
            if self.counter == k:
                self.k_smallest = curr.val
            
            dfs(curr.right, k)

        dfs(root, k)
        return self.k_smallest
            
        