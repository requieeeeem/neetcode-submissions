# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        #helper function
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q: #both are empty => same
                return True
            elif not p and q or not q and p: #one is empty, the other is not => not same
                return False
            elif p.val != q.val: #value differs => not same
                return False

            leftSame = isSameTree(p.left, q.left) #comparing left subtree
            rightSame = isSameTree(p.right, q.right) #comparing right subtree

            return (leftSame and rightSame) #true if both left and right subtree are the same

        if not root: #root is null, subtree won't be there
            return False
        if isSameTree(root, subRoot): #check if they're the same tree
            return True
        
        #recursively check left and right subtree
        subInLeft = self.isSubtree(root.left, subRoot)
        subInRight = self.isSubtree(root.right, subRoot)

        #if one is right, return True
        return subInLeft or subInRight