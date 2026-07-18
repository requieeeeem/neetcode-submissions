"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = { None : None} #be sure to initialize with None for edge cases

        #first iteration, make new node, then link old to new
        curr = head
        while curr:
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next

        #second iteration
        curr = head
        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next] 
            #which will point to the copy, because
            #example: oldToCopy[A.next] == oldToCopy[B] which points to B' (copy of B)
            copy.random = oldToCopy[curr.random]
            #same concept as above, curr.random would be evaluate first, which points to
            #an original node, which got hashed to the new map
            curr = curr.next
        
        return oldToCopy[head]

        