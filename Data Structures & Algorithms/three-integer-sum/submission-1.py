class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() #have to sort first
        sol = []
        for i in range(len(nums)):
            #since the list is sorted, doing this prevents duplication
            if nums[i] == nums[i - 1] and i > 0:
                continue
            target = -nums[i] #because nums[i] + nums[left] + nums[right] = 0
            left = i + 1 #both pointers start on the right side of the index
            right = len(nums) - 1
            while left < right:
                if (nums[left] + nums[right]) > target:
                    right -= 1
                elif (nums[left] + nums[right]) < target:
                    left += 1
                else:
                    sol.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # skip duplicate left values
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # skip duplicate right values
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                    
        return sol
