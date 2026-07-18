# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while slow and fast and fast.next:
            #stop if slow is null or fast is null or fast.next is null
            slow = slow.next
            fast = fast.next.next #jump 2 steps

            if slow == fast: #if they meet
                return True #there is a cycle, return true
        
        return False #one of the node reaches null, no cycle, return false