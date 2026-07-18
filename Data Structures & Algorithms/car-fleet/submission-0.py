class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pair = [[p,s] for p, s in zip(position, speed)]

        pair.sort() #need to sort it by position first

        for pos, speed in pair[::-1]: #[::-1] is called reverse splicing
            stack.append((target - pos) / speed)
            #if the time to reach destination is faster than the one in front of it, pop it
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
