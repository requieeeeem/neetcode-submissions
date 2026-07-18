# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #upper and lower bound in BST is for the whole subtree
        def dfs(node, upper, lower): #helper function to track upper and lower bound
            if not node:
                return True
            if node.val < upper and node.val > lower:
                return dfs(node.left, node.val, lower) and dfs(node.right, upper, node.val)
            else: return False

        return dfs(root, float('inf'), float('-inf'))