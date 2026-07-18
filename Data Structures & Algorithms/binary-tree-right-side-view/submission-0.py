# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        res = []
        
        if root:
            q.append(root)
        while q:
            qLen = len(q) #getting leng of queue to make sure we iterate through all of them
            for i in range(qLen): #using qLen here
                node = q.popleft() #first in first out
                if node.left: q.append(node.left) #add left and right to queue
                if node.right: q.append(node.right)
                if i == (qLen - 1): #if last node in level, add to result
                    res.append(node.val)
            

        return res