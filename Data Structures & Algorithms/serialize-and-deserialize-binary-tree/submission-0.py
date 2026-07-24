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
                self.preorder.append(None)
                return None
            
            self.preorder.append(curr.val)
            dfs(curr.left)
            dfs(curr.right)

        dfs(root)

        def to_string(preorder):
            output = ""
            for node_val in preorder:
                if node_val is None:
                    output += "null" + "."
                else:
                    output += str(node_val) + "."

            return output
        
        return to_string(self.preorder)
        

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]: 
        nodes = iter(data.split('.'))
        
        def build():
            val = next(nodes)
            if val == "null":
                return None
            
            node = TreeNode(int(val))
            node.left = build()
            node.right = build()

            return node
         

        root = build()
        return root


