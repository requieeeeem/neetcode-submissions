# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root: #base case, root is null
            return None

        if root.val > p.val and root.val > q.val: #curr > both => go down left side
            return self.lowestCommonAncestor(root.left, p, q) #don't forget to return
        if root.val < p.val and root.val < q.val: #curr < both => go down right side
            return self.lowestCommonAncestor(root.right, p, q)

        #curr lies between p and q, or equals to one of them
        return root