class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequency = [[] for i in range(len(nums) + 1)]
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        for num, freq in count.items():
            frequency[freq].append(num)

        sol = []
        for list in reversed(frequency):
            if list != []:
                for num in list:
                    sol.append(num)
                if len(sol) == k:
                    return sol