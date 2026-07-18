# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: #both are empty => same
            return True
        elif not p and q or not q and p: #one is empty, the other is not => not same
            return False
        elif p.val != q.val: #value differs => not same
            return False

        leftSame = self.isSameTree(p.left, q.left) #comparing left subtree
        rightSame = self.isSameTree(p.right, q.right) #comparing right subtree

        return (leftSame and rightSame) #true if both left and right subtree are the same