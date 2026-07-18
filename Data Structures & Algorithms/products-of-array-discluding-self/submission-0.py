class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [0] * length
        pre = [0] * length
        post = [0] * length
        pre[0] = 1 #no prefix product before first index
        post[length - 1] = 1 #no postfix product after last index
        for i in range(1, len(nums)): #pref[0] already set, running from 2nd index to last
            pre[i] = pre[i - 1] * nums[i - 1]
        for i in range(len(nums) - 2, -1, -1): #post[n-1] already set, running from next to last back to 1st
            post[i] = post[i + 1] * nums [i + 1]
        for i in range(len(nums)):
            result[i] = pre[i] * post[i]
        return result