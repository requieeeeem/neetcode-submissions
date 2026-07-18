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
            return "N" #use N if node is null
        #dfs
        result.append(str(root.val))
        result.append(self.serialize(root.left))
        result.append(self.serialize(root.right))

        print(','.join(result))
        return ','.join(result)
        

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        tree = data.split(",") #splitting list into comma seperated string
        index = 0 #global index
        def dfs(tree):
            nonlocal index #using the global index
            val = tree[index]
            index += 1 #auto increment every time the data is process

            if val == "N":
                return None

            node = TreeNode(val)
            node.left = dfs(tree) #with the increment index
            node.right = dfs(tree) #should be the right index after the left tree finished processing

            return node

        return dfs(tree)


