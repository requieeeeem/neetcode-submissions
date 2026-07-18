class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            #is the left half sorted
            if nums[left] <= nums[mid]:
                #is the target in the left half
                if nums[left] <= target < nums[mid]: #chained comparison, valid python syntax
                    #search left half
                    right = mid - 1
                else:
                    #search right half
                    left = mid + 1
            #left half is not sorted => right half is sorted
            else:
                #is the target in the right half
                if nums[mid] < target <= nums[right]:
                    #search right half
                    left = mid + 1
                else:
                    #search left half
                    right = mid - 1

        return -1