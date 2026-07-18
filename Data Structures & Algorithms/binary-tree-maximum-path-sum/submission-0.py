# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            leftCont = max(0, left) #if it's contribution is negative, don't use it
            rightCont = max(0, right)
            pathThru = leftCont + node.val + rightCont #treat the current node as the highest point
            #because the parent can't go both left and right
            self.res = max(pathThru, self.res) #updating the result

            return max(node.val + leftCont, node.val + rightCont)

        dfs(root)
        return self.res
            

            