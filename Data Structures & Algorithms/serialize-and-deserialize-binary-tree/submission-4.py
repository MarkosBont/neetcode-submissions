# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.preorder = []

        def dfs(curr):
            if not curr:
                self.preorder.append("null")
                return None
            
            self.preorder.append(str(curr.val))
            dfs(curr.left)
            dfs(curr.right)

        dfs(root)
        
        return ".".join(self.preorder)
        

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]: 
        nodes = data.split('.')
        self.i = 0
        
        def build():
            val = nodes[self.i]
            if val == "null":
                self.i += 1
                return None
            
            node = TreeNode(int(val))
            self.i += 1
            node.left = build()
            node.right = build()

            return node
         
        return build()


