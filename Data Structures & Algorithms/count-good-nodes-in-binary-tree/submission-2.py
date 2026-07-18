# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        #helper function
        def dfs(node, currMax):
            #base case
            if not node: #empty tree has no good node
                return 0
            
            res = 1 if node.val >= currMax else 0 
            currMax = max(currMax, node.val) #updating currMax for that path
            #recursive case
            res += dfs(node.left, currMax) #check left
            res += dfs(node.right, currMax) #check right
            return res

        return dfs(root, root.val) #root is always a good node => starts at root.val