# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#FIXMEEEE
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newHead: ListNode
        curr1, curr2 = list1, list2
        #when one of the 2 lists is empty, return the other
        if list1 is None: 
            return list2
        if list2 is None:
            return list1
        #check initial value, then attach head, then move that list pointer
        if list1.val < list2.val:
            newHead = list1
            curr1 = curr1.next
        else:
            newHead = list2
            curr2 = curr2.next
        curr = newHead
        while curr1 is not None and curr2 is not None:
            if curr1.val < curr2.val:
                curr.next = curr1
                curr = curr.next
                curr1 = curr1.next
            else:
                curr.next = curr2
                curr = curr.next
                curr2 = curr2.next
        if curr1 is None:
            curr.next = curr2
        else:
            curr.next = curr1

        return newHead