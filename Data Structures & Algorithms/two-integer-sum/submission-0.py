class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        resultSet = {}

        for i, num in enumerate(nums):
            difference = target - nums[i]
            if difference in resultSet:
                return [resultSet[difference], i]
            else:
                resultSet[nums[i]] = i