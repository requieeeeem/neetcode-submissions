# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #start at head
        first = head

        #move ahead n nodes
        for i in range(n):
            first = first.next

        #dummy, to track start of list
        dummy = ListNode()
        dummy.next = head #will always point to head of new list
        second = dummy #always stay n + 1 node behind first
        while first:
            first = first.next
            second = second.next

        second.next = second.next.next #remove the next node

        return dummy.next