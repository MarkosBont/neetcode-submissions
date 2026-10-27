# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.kth = None
        self.visited = 0

        def dfs(curr):
            if not curr:
                return None

            dfs(curr.left)

            self.visited += 1
            if self.visited == k:
                self.kth = curr.val

            dfs(curr.right)

        dfs(root)
        return self.kth
        