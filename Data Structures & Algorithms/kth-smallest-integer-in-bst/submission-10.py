# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.counter = 0
        self.result = None

        def in_order(curr):
            if not curr:
                return None
            
            in_order(curr.left)

            self.counter += 1
            if self.counter == k:
                self.result = curr.val
            
            in_order(curr.right)
        
        in_order(root)
        return self.result
        