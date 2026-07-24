# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
            
        q = deque()
        q.append(root)

        while q:
            local = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    local.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            
            if local:
                result.append(local)
        
        return result





        