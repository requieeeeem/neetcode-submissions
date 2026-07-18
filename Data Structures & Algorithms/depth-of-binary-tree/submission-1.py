# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: #if node is null, don't add depth
            return 0
        
        leftDepth = self.maxDepth(root.left) #find depth of left recursively
        rightDepth = self.maxDepth(root.right) #find depth of right recursively

        return max(leftDepth, rightDepth) + 1 #add one from the root
        