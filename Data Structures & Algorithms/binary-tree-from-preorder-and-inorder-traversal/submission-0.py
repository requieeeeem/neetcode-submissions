# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #base case
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0]) #creating a new node
        mid = inorder.index(root.val) #finding the node index in inorder
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid]) #left tree = left of mid in inorder
        #length of subtree is the same in both traversal list
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:]) #right tree = right of mid in inorder

        return root