import math #for math.ceil, for rounding up

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1 #minimum koko could eat in 1 hour
        high = max(piles) #maximum koko could eat in 1 hour, any faster wouldn't matter
        result = high #cuz we know this would always work

        while low <= high:
            mid = (low + high) // 2 #test value, not the answer
            time = 0
            for pile in piles:
                time += math.ceil(pile/mid) #time to eat one pile, use ceil to round up
            if time <= h:
                result = min(result, mid)
                high = mid - 1
            else:
                low = mid + 1
        
        return result