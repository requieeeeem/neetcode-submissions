class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        solFound = False
        while not solFound:
            if ((numbers[left] + numbers[right]) > target):
                right -= 1
            elif ((numbers[left] + numbers[right]) < target):
                left += 1
            else:
                solFound = True

        return [left + 1, right + 1] 