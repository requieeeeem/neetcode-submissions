class Solution:
    #Floyd's cycle detection algo
    def findDuplicate(self, nums: List[int]) -> int:
        #treat next_position = nums[current_position]
        slow = nums[0]
        fast = nums[0]

        slow = nums[slow] #like slow = slow.next
        fast = nums[nums[fast]] #like fast = fast.next.next
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        slow = nums[0] #reseting the pointer
        while slow != fast:
            #moving one step at a time until they meet again
            slow = nums[slow]
            fast = nums[fast]

        return slow #or fast