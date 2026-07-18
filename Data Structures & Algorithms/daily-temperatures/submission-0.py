# monotonic decreasing stack
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  # [temp, index]
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:  # checking temps
                result[stack[-1][1]] = i - stack[-1][1]  # result = current index - stored index
                stack.pop()
            stack.append([temperatures[i], i])

        return result
