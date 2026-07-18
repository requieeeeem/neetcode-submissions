#monotonically increasing stack
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for index, height in enumerate(heights):
            start = index #to track if you can move it backwards

            #while height in stack > current height
            #check the maxArea
            while stack and stack[-1][1] > height: 
                i, h = stack.pop()
                maxArea = max(maxArea, h * (index - i)) #index = curr Index, i = index of pop, h = pop height
                start = i #extending the index backwards
            stack.append((start, height))

        for index, height in stack:
            maxArea = max(maxArea, (len(heights) - index) * height)

        return maxArea