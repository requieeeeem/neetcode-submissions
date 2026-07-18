# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        res = []
        

        q.append(root)
        while q:
            qLen = len(q) #getting leng of queue to make sure we iterate through all of them
            currLvl = []
            for i in range(qLen): #using qLen here
                node = q.popleft() #first in first out
                if node: #not null
                    currLvl.append(node.val)
                    q.append(node.left) #add left and right to queue
                    q.append(node.right)
            if currLvl: #add if the list for the level is not empty
                res.append(currLvl)

        return res