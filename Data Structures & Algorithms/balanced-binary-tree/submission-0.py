# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            return 1 + max(left, right)
    
        
        left_height = dfs(root.left)
        right_height = dfs(root.right)

        if -1 <= left_height - right_height <= 1:
            print(left_height, right_height)
            return True
        else:
            return False
        