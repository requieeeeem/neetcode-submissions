class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numCollection = set(nums)
        longest = 1
        for i in range(len(nums)):
            if (nums[i] - 1) not in numCollection:
                curr = nums[i]
                print(curr)
                counter = 1
                while (curr + 1) in numCollection:
                    counter += 1
                    curr += 1
                if counter > longest:
                    longest = counter


        return longest