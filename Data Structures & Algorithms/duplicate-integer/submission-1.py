class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        thisset = set()
        for num in nums:
            if num not in thisset:
                thisset.add(num)
            else: return True
        return False
        