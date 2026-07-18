# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root: #if null, stop
            return None

        root.right, root.left = root.left, root.right #swap left and right
        self.invertTree(root.left) #recursively calling the function
        self.invertTree(root.right)

        return root