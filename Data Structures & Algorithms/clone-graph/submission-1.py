"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(curr):
            if not curr:
                return None
            
            if curr in oldToNew:
                return oldToNew[curr]

            new = Node(curr.val)
            oldToNew[curr] = new
            for nei in curr.neighbors:
                new.neighbors.append(dfs(nei))
            
            return new
        
        return dfs(node)