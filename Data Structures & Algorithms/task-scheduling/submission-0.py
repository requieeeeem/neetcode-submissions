#NONE HEAP SOLUTION
from collections import Counter #to count the frequency

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxFreq = max(freq.values()) #to find the maximum frequency
        maxCount = sum(1 for frequency in freq.values() if frequency == maxFreq) #count of task with max frequency
        #the least amount of space needed to satisfy the n cycle requirement for the tasks with the highest frequency
        skeleton = (maxFreq - 1) * (n + 1) + maxCount
        return max(len(tasks), skeleton)