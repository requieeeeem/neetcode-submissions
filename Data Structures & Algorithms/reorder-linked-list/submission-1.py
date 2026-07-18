# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next #jump 2 times
        #after this, slow will point to the middle of the linked list

        second = slow.next
        slow.next = None
        #cutting the connection

        #reversing the second part
        curr = second
        prev = None
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        #prev now points to the 2nd part head

        first = head #head of first half
        second = prev #head of second half
        

        #linking them alternately, due to the way it's split, if it's odd
        #there's gonna be extra node from the first
        while second:
            nextFirst = first.next
            nextSecond = second.next

            first.next = second
            second.next = nextFirst

            first = nextFirst
            second = nextSecond



        