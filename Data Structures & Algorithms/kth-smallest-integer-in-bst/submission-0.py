# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        
        def inorder(node):
            if not node:
                return
            #inorder = left => root => right
            inorder(node.left)
            stack.append(node.val)
            inorder(node.right)

        inorder(root)


        return stack[k-1] #kth smallest = k - 1 index (0 index = smallest), stack gonna be from smallest to largest
