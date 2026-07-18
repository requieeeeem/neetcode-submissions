class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        sol = 0
        #block to check maxLeft
        for i in range(len(height)):
            if i == 0:
                maxLeft[i] = 0
            elif height[i - 1] >= maxLeft[i - 1]:
                maxLeft[i] = height[i - 1]
            else:
                maxLeft[i] = maxLeft[i - 1]
        #block to check maxRight
        for i in range(len(height) - 1, -1, -1):
            if i == (len(height) - 1):
                maxRight[i] = 0
            elif height[i + 1] >= maxRight[i + 1]:
                maxRight[i] = height[i + 1]
            else:
                maxRight[i] = maxRight[i + 1]
        
        for i in range(len(height)):
            waterAmount = min(maxLeft[i], maxRight[i]) - height[i]
            if waterAmount > 0:
                sol += waterAmount
        return sol
