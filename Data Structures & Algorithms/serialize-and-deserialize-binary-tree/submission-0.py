# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []
        if not root:
            return "N"
        
        result.append(str(root.val))
        result.append(self.serialize(root.left))
        result.append(self.serialize(root.right))

        print(','.join(result))
        return ','.join(result)
        

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        tree = data.split(",")
        index = 0
        def dfs(tree):
            nonlocal index
            val = tree[index]
            index += 1

            if val == "N":
                return None

            node = TreeNode(val)
            node.left = dfs(tree)
            node.right = dfs(tree)

            return node

        return dfs(tree)


