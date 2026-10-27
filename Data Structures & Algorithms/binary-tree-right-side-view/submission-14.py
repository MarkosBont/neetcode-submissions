# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque([root])
        right_values = []

        while q:
            this_level = []
            for i in range(len(q)):
                element = q.popleft()
                this_level.append(element.val)

                if element.left:
                    q.append(element.left)
                
                if element.right:
                    q.append(element.right)

            rightest = this_level[-1]
            right_values.append(rightest)
        
        return right_values
