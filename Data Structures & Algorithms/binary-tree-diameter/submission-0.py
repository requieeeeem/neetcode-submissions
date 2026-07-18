# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0 #global variable to keep track, outside of recursion

        def maxDepth(curr: Optional[TreeNode]) -> int: #from last problem
            if not curr: #if node is null, don't add depth
                return 0
            
            leftDepth = maxDepth(curr.left) #find depth of left recursively
            rightDepth = maxDepth(curr.right) #find depth of right recursively

            self.res = max(self.res, leftDepth + rightDepth)

            return max(leftDepth, rightDepth) + 1 #add one from the root
        
        maxDepth(root)
        return self.res