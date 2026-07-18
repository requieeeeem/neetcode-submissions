from collections import deque
#use queue to add and remove in O(1) time from both ends
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = right = 0
        result = []
        q = deque() #important to store indices, not value, in decreasing value order
        while right < len(nums):
            #while q is not empty and right most number in queue < the number being added
            #pop it
            #highest number will always stay on the left
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)
            
            if right - left + 1 == k: #when length == k
                result.append(nums[q[0]]) #add the left most (aka the max) to the result list
                left += 1 #move left
                if q[0] < left: #if the index is smaller than current left pointer, pop it
                    q.popleft()

            right += 1
        return result