# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        groupPrev = dummy
        

        while True:
            kthNode = self.getKNode(groupPrev, k)
            if not kthNode:
                break
            groupNext = kthNode.next

            curr = groupPrev.next
            prev = groupNext
            while curr != groupNext:
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode

            temp = groupPrev.next #gonna be the new head of the reverse list
            #also change dummy.next for the first iteration
            groupPrev.next = kthNode
            groupPrev = temp

        return dummy.next


    #helper function to find kth Node
    def getKNode(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
                

        