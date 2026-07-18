# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: #empty tree is balanced
            return True

        def maxDepth(curr: Optional[TreeNode]) -> int: #from last problem
            if not curr: #if node is null, don't add depth
                return 0
            
            leftDepth = maxDepth(curr.left) #find depth of left recursively
            rightDepth = maxDepth(curr.right) #find depth of right recursively

            return max(leftDepth, rightDepth) + 1 #add one from the root

        left = maxDepth(root.left) #find height left
        right = maxDepth(root.right)#find height right

        if abs(left - right) > 1: #absolute to make sure it works if right > left
            return False #more than 1 => not balanced
        #else recursively check left and right
        else: return self.isBalanced(root.left) and self.isBalanced(root.right) 